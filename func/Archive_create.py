import os
from func.Sistem_func import *
import shutil


def ctarch(*args):
    name = args[0]
    root_dir = args[1]
    check_path(root_dir)
    formatt = 'zip'
    try:
        shutil.make_archive(name, root_dir=root_dir, format=formatt)
    except FileNotFoundError as err:
        print(err)
