import os
from func.Sistem_func import *
import shutil
from Sistem_var import *

def unarch(*args):
    name = os.getcwd()+'\\'+args[0]
    check_path(name)
    formatt = None
    extract_dir = None
    for i in args[1:]:
        if "extract_dir" in i: extract_dir = i.split('=')[1]
        if "format" in i: formatt = i.split('=')[1]
    if extract_dir is None: extract_dir = os.getcwd()
    try:
        if formatt is None:
            shutil.unpack_archive(name, extract_dir=extract_dir)
        else:
            shutil.unpack_archive(name, extract_dir=extract_dir, format=formatt)
    except shutil.ReadError as err:
        print(err)