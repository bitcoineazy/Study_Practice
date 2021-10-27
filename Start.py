import os
from Sistem_var import *
def end():
    exit()


work_path = Work_path[0]

print(work_path)
def Start():
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
