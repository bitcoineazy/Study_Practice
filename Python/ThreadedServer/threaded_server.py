import socket
import hashlib
import json
import pickle
from threading import Thread
import logging
from port_validation import port_validation, is_available_port

PORT_DEFAULT = 9090
logging.basicConfig(format="%(asctime)s [%(levelname)s] %(funcName)s: %(message)s",
                    handlers=[logging.FileHandler("log/threaded_server.log"), logging.StreamHandler()], level=logging.INFO)


class Server:
    def __init__(self, port):
        self.database = "./users.json"
        self.clients = []
        self.server_port = port
        self.users = []
        self.init_server()

    def init_server(self):
        """
        Запуск сервера
        """
        sock = socket.socket()
        sock.bind(('', self.server_port))
        sock.listen(5)
        self.sock = sock
        logging.info(f"Сервер стартанул, слушаем порт {self.server_port}")
        while True:
            conn, addr = self.sock.accept()
            Thread(target=self.client_logic, args=(conn, addr)).start()
            print(f"Подключение клиента {addr}")
            logging.info(f"Подключение клиента {addr}")
            self.clients.append(conn)

    def broadcast(self, msg, conn, address, username):
        """
        Отправка данных клиентам
        """
        username += "_" + str(address[1])
        for sock in self.clients:
            if sock != conn:
                data = pickle.dumps(["message", msg, username])
                sock.send(data)
                print(f"Отправка данных клиенту {sock.getsockname()}: {msg}")
                logging.info(f"Отправка данных клиенту {sock.getsockname()}: {msg}")

    def client_logic(self, conn, address):
        """
        Слушаем подключения, если данные есть отправляем их клиентам.
        Если данных нету закрываем соединение с клиентом.
        """
        self.authorization(address, conn)
        while True:
            try:
                data = conn.recv(1024)
            except ConnectionResetError:
                conn.close()
                self.clients.remove(conn)
                print(f"Отключение клиента {address}")
                logging.info(f"Отключение клиента {address}")
                break
            if data:
                status, data, username = pickle.loads(data)
                print(f"Прием данных от клиента '{username}_{address[1]}': {data}")
                logging.info(f"Прием данных от клиента '{username}_{address[1]}': {data}")
                if status == "message":
                    self.broadcast(data, conn, address, username)
            else:
                # Закрываем соединение
                conn.close()
                self.clients.remove(conn)
                logging.info(f"Отключение клиента {address}")
                break

    def authorization(self, addr, conn):
        # Проверка есть ли в файле данные
        try:
            self.users = self.json_read()
        except json.decoder.JSONDecodeError:
            self.registration(addr, conn)
        is_registered = False
        for user in self.users:
            if addr[0] in user:
                for k, v in user.items():
                    if k == addr[0]:
                        name = v['name']
                        password = v['password']
                        conn.send(pickle.dumps(["passwd", "Введите свой пароль: "]))
                        passwd = pickle.loads(conn.recv(1024))[1]
                        conn.send(pickle.dumps(["success", f"Здравствуйте, {name}"])) if self.check_password(
                            passwd, password) else self.authorization(addr, conn)
        if not is_registered:
            self.registration(addr, conn)

    def registration(self, addr, conn):
        conn.send(pickle.dumps(
            ["auth", ""]))
        name = pickle.loads(conn.recv(1024))[1]
        conn.send(pickle.dumps(["passwd", "Введите свой пароль: "]))
        passwd = self.generate_hash(pickle.loads(conn.recv(1024))[1])
        conn.send(pickle.dumps(["success", f"Приветствую, {name}"]))
        self.users.append({addr[0]: {'name': name, 'password': passwd}})
        # Запись в файл при регистрации пользователя
        self.json_write()
        self.users = self.json_read()

    def json_read(self):
        with open(self.database, 'r') as f:
            users = json.load(f)
        return users

    def json_write(self):
        with open(self.database, 'w') as f:
            json.dump(self.users, f, indent=4)

    def check_password(self, passwd, userkey):
        """
        Проверка пароля из файла и введенный пользователем
        """
        key = hashlib.md5(passwd.encode() + b'salt').hexdigest()
        return key == userkey

    def generate_hash(self, passwd):
        """
        Генерация хэш-пароля
        """
        key = hashlib.md5(passwd.encode() + b'salt').hexdigest()
        return key


def main():
    server_port = PORT_DEFAULT
    # Если порт по умолчанию занят, то перебираем порты
    if not port_validation(PORT_DEFAULT, True):
        if not is_available_port(PORT_DEFAULT):
            print(f"Порт по умолчанию {PORT_DEFAULT} занят")
            logging.info(f"Порт по умолчанию {PORT_DEFAULT} занят")
            port_available = False
            while not port_available:
                server_port += 1
                port_available = is_available_port(server_port)
    try:
        Server(server_port)
    except KeyboardInterrupt:
        logging.info(f"Остановка сервера")


if __name__ == "__main__":
    main()
