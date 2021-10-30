import socket


def port_validation(port, check_available=False):
    try:
        value = int(port)
        if 1 <= value <= 65535:
            # Проверка доступности порта
            if check_available:
                return is_available_port(value)
            print(f"Port: {value} - correct, proceeding to the next step")
            return True
        print(f"Wrong value: {value} for port")
        return False
    except ValueError:
        print(f"Port: {port} - not a number!")
        return False


def is_available_port(port):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if conn.connect_ex(('localhost', port)):
        conn.close()
        print(f"Порт {port} свободен")
        return True
    else:
        print(f"Порт {port} занят")
        return False
