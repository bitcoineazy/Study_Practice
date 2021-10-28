from func import *
from Start import *
from Input import *
from Sistem_var import *

HELP = f"""Файловый менеджер - программа для простой работы с файлами
В настройках указывается путь к рабочей папке
Работа с файлами вне рабочей директории невозможна
Доступные команды: getcom
Полную справку о командах можно получить по команде: cominf
"""
comand_name = ['ctdir', 'getcom', "Exit", 'help', 'cominf',
               'deldir', 'cdd', 'lsdir', 'ctfile', 'nano2',
               'cutfile', 'delfile', 'mvfile', 'refile', 'ctarch',
               'unarch', 'unafor']
COMINF = """-----
help: общая справка
getcom: показывает доступные команды
newdir [path]: создает новую директорию по указанному пути
    path - путь к создаваемой директории
ctdir [path]: создает директорию
deldir [path]: удаляет директорию
cdd [path]: изменяет текушую директорию
lsdir: показывает содержиаое директории
ctfile [path]: создает новый файл по указанному пути
nano2 [path, mod]: открывает файл для дозаписи mod='a'(по умолчанию) или перезаписывает его mod='w'
cutfile [path]: выврд содержимого файла
delfile [path]: удаляет файл по указанному пути
mvfile [path_out, path_to]: path_out - файл для перемешения, path_to - директория куда переместить
refile [path]: переименовывает файл
Exit: завершение работы программы
-----"""
def help():
    print(HELP, end='')

def getcom():
    print("Доступные команды:")
    print(splitls(comand_name))


def cominf():
    print(COMINF)

def input_mod(var):
    if var == True:
        Mod_out[0]=True
    elif var == False:
        Mod_out[0]=False
    else:
        print('Неверно указанный параметр')


nameoffunc = [name for (name, obj) in vars().items()
       if hasattr(obj, "__class__") and obj.__class__.__name__ == "function" and name in comand_name]

functioninc = [obj for (name, obj) in vars().items()
       if hasattr(obj, "__class__") and obj.__class__.__name__ == "function" and name in comand_name]

dictcommand = dict(zip(nameoffunc, functioninc))

#print([name for (name, obj) in vars().items() if hasattr(obj, "__class__") and obj.__class__.__name__ == "function"])
#print(dictcommand)


if __name__ == '__main__':
    Start()
    k = 0
    while True:
        inp = Input()
        if inp[0] in comand_name:
            try:
                dictcommand[inp[0]](*inp[1:])
            except TypeError as err:
                print(err)
            except AssertionError as err:
                print(err)
        else:
            print('Неверно введенная команда \nСписок доступных команд: getcom')
        k += 1


