import os
import pickle
from Sistem_var import *
def end():
    exit()


def Start():

    name = input('Login: ')
    def chek_name(name):
        with open('Setting.txt', 'a+', encoding="utf-8") as f:
            f.seek(0, 0)
            for i in f.readlines():
                s = i.split()
                if name == s[0]:
                    return name
            else:
                f.write(f'{name} None\n')
                return name
    name = chek_name(name)
    work_path = get_work_path(name)
    if 'None' in work_path:
        work_path = input('Set path for dir: ')
        with open('Setting.txt', 'r+', encoding="utf-8") as f:
            k = f.readlines()
            for i in range(len(k)):
                line = k[i].split(' ')
                if line[0] == name:
                    if line[1][-2:] == '\n':
                        line[1] = work_path + '\n'
                    else:
                        line[1] = work_path
                    k[i] = f'{line[0]} {line[1]}\n'
                    break
        with open('Setting.txt', 'w', encoding="utf-8") as f:
            for i in k:
                f.write(i)


    print('Путь к файлу рабочей директории:', work_path)
    try:
        os.chdir(work_path)
    except FileNotFoundError:
        print("Данная директории не существует")
        while True:
            k = input("Создать директорию? (y/n)\n")
            k = k.lower()
            if k == 'exit' or k == 'выход':
                end()
            if k == 'y' or k == "д":
                try:
                    os.makedirs(work_path)
                except PermissionError:
                    print("Увас нет прав на совершение этого действия выберите другую директорию")
                    end()
                os.chdir(work_path)
                break
            elif k == "n" or k == 'н':
                print("Создайте указанную директорию вручную или укажите новую")
                end()
            else:
                print('Ваш ответ некоректен укажите либо y-Да либо n-Нет')
