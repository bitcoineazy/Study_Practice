import os
from func.Sistem_func import *
def cdd(path):
    check_path(path)
    try:
        os.chdir(path)
    except OSError as err:
        print(err)