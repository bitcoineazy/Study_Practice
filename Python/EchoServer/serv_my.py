import json
import random
import socket
from threading import Thread
import logging
from utilities import COLORS, EMOJIS, EMOJIS_PATTERN, SocketMethods, Security

logging.basicConfig(filename='server_logs.log', level=logging.INFO)

users = {}
logins = {}
connections_list = []


class ClientThread(Thread):
    def __init__(self, connection, address):
        super().__init__(daemon=True)
        self.connected = True
        self.conn = connection
        self.addr = address
        self.username = None
        self.color = random.choice(COLORS)
        self.login()

    def login(self):
        self.send_msg('Введите имя пользователя')
        name = self.receive_msg()
        self.username = name
        if name in users.keys():
            self.send_msg('Enter password')
            if users[name]['password'] == Security.get_password_hash(self.receive_msg()):
                self.success_login()
            else:
                self.close_connection('incorrect password')
        else:
            self.send_msg('Set new password')
            users.update({name: {'password': Security.get_password_hash(self.receive_msg())}})
            save_users()
        logins.update({addr[0]: name})
        save_logins()

    def success_login(self):
        self.send_msg(f'Success login')
        save_users()

    def close_connection(self, reason='', only_server=False):
        if not only_server:
            self.send_msg(f'Closing connection {self.addr} {" because of " + reason if reason else ""}')
            self.send_msg('//close')
            self.conn.close()
        print(f'Connection closed {self.addr} {" - " + reason if reason else ""}')
        logging.info(f'Connection closed {self.addr} {" - " + reason if reason else ""}')
        self.connected = False
        if self in connections_list:
            connections_list.remove(self)

    def send_msg(self, message):
        if self.connected:
            SocketMethods.send_text(self.conn, message)

    def receive_msg(self):
        if not self.connected:
            return
        try:
            return SocketMethods.receive_text(self.conn)
        except ConnectionResetError:
            self.close_connection('connection error', only_server=True)

    def run(self):
        connections_list.append(self)
        self.send_msg(f'{self.username}, welcome to chat')
        service_msg(self, 'joined the chat')

        while True and self.connected:
            message = self.receive_msg()
            if message == 'exit':
                self.close_connection('user exit')
                break
            send_msg_all(f'{self.color}{self.username}\33[0m: {emoji_replace(message)}')


def save_users():
    with open('users.json', 'w') as file:
        json.dump(users, file)


def save_logins():
    with open('logins.json', 'w') as file:
        json.dump(logins, file)


def send_msg_all(message):
    [i.send_msg(message) for i in connections_list]


def service_msg(user, message):
    [i.send_msg(f'\33[4m{user.username} {message}\33[0m') for i in connections_list if i != user]


def _emoji_replace(match):
    mg = match.group(1)
    return EMOJIS.get(mg, f':{mg}:')


def emoji_replace(s):
    return EMOJIS_PATTERN.sub(_emoji_replace, s)


if __name__ == '__main__':
    sock = socket.socket()
    port = 9000
    while True:
        try:
            sock.bind(('', port))
            break
        except OSError:
            port += 1
    print(f'Started on {socket.gethostbyname(socket.gethostname())}:{port}')
    logging.info(f'Started on {socket.gethostbyname(socket.gethostname())}:{port}')
    sock.listen(10)

    with open('users.json', 'r') as file:
        users = json.load(file)
    with open('logins.json', 'r') as file:
        logins = json.load(file)
    while True:
        # Создать новые потоки для пользователей
        conn, addr = sock.accept()
        print(f'Opening connection {addr} ')
        logging.info(f'Opening connection {addr} ')
        thread = ClientThread(conn, addr)

        thread.start()
