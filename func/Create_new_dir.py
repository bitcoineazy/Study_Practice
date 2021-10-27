import os
from func.Sistem_func import *

def ctdir(path):
    check_path(path)
    try:
        os.makedirs(path)
    except OSError as err:
        print(err)
