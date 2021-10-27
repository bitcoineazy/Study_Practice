import os
from func.Sistem_func import *
def ctfile(path):
    check_path(path)
    if os.access(path, os.F_OK):
        print('Указаный файл уже существует')
        return False
    f = open(path, 'a')
    f.close()