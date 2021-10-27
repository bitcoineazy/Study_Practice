import os
from func.Sistem_func import *

def deldir(path):
    check_path(path)
    try:
        os.rmdir(path)
    except OSError as err:
        print(err)
