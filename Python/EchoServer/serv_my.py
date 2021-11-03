import json
import random
import socket
from threading import Thread
import logging
import hashlib

logging.basicConfig(filename='server_logs.log', level=logging.INFO)

users = {}
logins = {}
connections_list = []
ENCODING = 'utf-8'
SALT = 'salt'.encode('utf-8')
COLORS = ['\33[31m', '\33[32m', '\33[33m', '\33[34m', '\33[35m', '\33[36m', '\33[91m', '\33[92m', '\33[93m', '\33[94m',
          '\33[95m', '\33[96m']


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
            if users[name]['password'] == get_password_hash(self.receive_msg()):
                self.success_login()
            else:
                self.close_connection('incorrect password')
        else:
            self.send_msg('Set new password')
            users.update({name: {'password': get_password_hash(self.receive_msg())}})
            save_users()
        logins.update({addr[0]: name})
        save_logins()

    def success_login(self):
        self.send_msg(f'Success login')
        save_users()

    def close_connection(self, reason=''):
        logging.info(f'Connection closed {self.addr} {" - " + reason if reason else ""}')
        self.connected = False
        if self in connections_list:
            connections_list.remove(self)

    def send_msg(self, message):
        if self.connected:
            send_text(self.conn, message)

    def receive_msg(self):
        if not self.connected:
            return
        try:
            return receive_text(self.conn)
        except ConnectionResetError:
            self.close_connection('connection error')

    def run(self):
        connections_list.append(self)
        self.send_msg(f'{self.username}, welcome to chat')
        service_msg(self, 'joined the chat')

        while True and self.connected:
            message = self.receive_msg()
            if message == 'exit':
                self.close_connection('user exit')
                break
            send_msg_all(f'{self.color}{self.username}\33[0m: {message}')


def save_users():
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)


def save_logins():
    with open('logins.json', 'w') as f:
        json.dump(logins, f, indent=4)


def send_msg_all(message):
    [i.send_msg(message) for i in connections_list]


def service_msg(user, message):
    [i.send_msg(f'\33[4m{user.username} {message}\33[0m') for i in connections_list if i != user]


def get_password_hash(password):
    return hashlib.sha512(password.encode('utf-8') + SALT).hexdigest()


def receive_text(conn):
    return conn.recv(1024).decode(ENCODING)


def send_text(conn, message):
    message = message.encode(ENCODING)
    conn.send(message)


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
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except json.decoder.JSONDecodeError:
        users = {}
    with open('logins.json', 'r') as file:
        logins = json.load(file)
    while True:
        # Создать новые потоки для пользователей
        conn, addr = sock.accept()
        print(f'Opening connection {addr} ')
        logging.info(f'Opening connection {addr} ')
        thread = ClientThread(conn, addr)

        thread.start()
