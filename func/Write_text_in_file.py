import os
from func.Sistem_func import *
from func.Cutfile import cutfile

def nano2(path, mod='a'):
    check_path(path)
    f = open(path, mod)
    print('Для остановки записи введите quit()')
    if mod == 'a':
        cutfile(path)
    while True:
        text = input()+'\n'
        if text[-7:] == 'quit()\n':
            print('Конец записи')
            break
        f.write(text)
    f.close()