import shutil
from func.Sistem_func import *
import os

def mvfile(path_out, path_to):
    check_path(path_out)
    check_path(path_to)
    try:
        shutil.move(path_out, path_to)
    except shutil.Error as err:
        print(err)