import os
from func.Sistem_func import *

def refile(path):
    check_path(path)
    try:
        os.rename(path)
    except OSError as err:
        print(err)
