import os
from func.Sistem_func import *
import shutil


def ctarch(*args):
    name = args[0]
    root_dir = args[1]
    check_path(root_dir)
    base_dir = None
    formatt = 'zip'
    for i in args[2:]:
        if "format" in i: formatt = i.split('=')[1]
    try:
        shutil.make_archive(name, root_dir=root_dir, format=formatt)
    except FileNotFoundError as err:
        print(err)
