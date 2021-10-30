import os
import socket
import sys
from threading import Thread
from utilities import SocketMethods
from validators import ipv4

sock = socket.socket()


def port_validation(port):
    try:
        if 1023 < int(port) < 65536:
            return True
        else:
            return False
    except ValueError:
        return False


address = input('Input IP address: ')
if not address:
    address = 'localhost'
elif not ipv4(address):
    print('Wrong IP address')
port = input('Input port: ')
if not port:
    port = 9000
elif not port_validation(port):
    print('Wrong port input\nTry ports with number 1024 - 65535')
else:
    port = int(port)

sock.connect((address, port))
os.system('')

try:
    with open('token', 'r') as file:
        token = file.read()
except FileNotFoundError:
    token = '--no token--'
SocketMethods.send_text(sock, token)

connection_alive = True


def custom_input():
    result = ''
    if os.name == 'nt':
        import msvcrt
        while True:
            entered = msvcrt.getwch()
            if entered == '\r':
                break
            msvcrt.putwch(entered)
            result += entered
    else:
        import curses
        console = curses.initscr()
        while True:
            entered = console.get_wch()
            if entered == '\n':
                break
            result += entered
    print('\r', flush=False, end='')
    # print('>', result)
    return result


def receive_messages():
    global connection_alive
    while True:
        received = SocketMethods.receive_text(sock)
        if received[:2] == '//':
            if received == '//close':
                sock.close()
                connection_alive = False
                break
            if received == '//token':
                with open('token', 'w') as file:
                    file.write(SocketMethods.receive_text(sock))
                continue
        print(received)
    sys.exit()


Thread(target=receive_messages, daemon=True).start()

while True:
    message = custom_input()
    if connection_alive:
        SocketMethods.send_text(sock, message)
    else:
        break
