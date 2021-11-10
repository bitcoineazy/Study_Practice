import os
from func.Sistem_func import *

def refile(path, new_name):
    check_path(path)
    try:
        os.rename(path, new_name)
    except OSError as err:
        print(err)
