import shutil
from func.Sistem_func import splitls
def getafor():
    print(splitls([i for i, f in shutil.get_archive_formats()], column=3))