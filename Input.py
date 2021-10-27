import os
from Sistem_var import *
from func.Show_my_dir_now import lsdir
def Input():
    pathdir = f"{os.path.relpath(os.getcwd(), start=Work_path[0])}"
    if pathdir[0] == '.':
        pathdir = '~: >'
    else:
        pathdir = '~:' + pathdir
        pathdir = f'{pathdir}>'
    if Mod_out[0]:
        lsdir(os.getcwd())
    comand = input(pathdir).split()
    return comand