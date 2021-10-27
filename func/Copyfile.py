import shutil
import os
from func.Sistem_func import *

def cpfile(path_out, path_to):
    check_path(path_out)
    check_path(path_to)
    if os.path.isfile(path_out):
        if os.path.isdir(path_to):
            try:
                shutil.copy(path_out, path_to)
            except FileNotFoundError as err:
                print(err)
            except shutil.SameFileError as err:
                print(err)
            except shutil.SpecialFileError as err:
                print(err)
            except shutil.Error as err:
                print(err)
        else:
            print(f"{path_to} не директоря")
    else:
        print(f"{path_out} не файл")