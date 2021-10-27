import os
from func.Sistem_func import *
def delfile(path):
    check_path(path)
    if os.path.isfile(path):
        try:
            os.remove(path)
        except OSError as err:
            print(err)
    else:
        print("Путь указывает на директорию\nВоспользуйтесь номендой deldir")
