import shutil
from func.Sistem_func import *

def copyfile(path_out, path_to):
    check_path(path_out)
    check_path(path_to)
    try:
        shutil.copy2(path_out, path_to)
    except shutil.SameFileError as err:
        print(err)