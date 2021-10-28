import shutil
from func.Sistem_func import splitls
def unafor():
    print(splitls([i for i, j, k in shutil.get_unpack_formats()], column=3))