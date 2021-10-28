from func.Sistem_func import *

def cutfile(path):
    check_path(path)
    try:
        with open(path, mode='r') as f:
            print(*f.readlines(), sep='', end='')
    except FileNotFoundError as err:
        print(err)
