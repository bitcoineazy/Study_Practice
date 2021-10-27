import os
from func.Sistem_func import *
import time
def nmod():
    if len(os.listdir()) == 0:
        return ''
    return splitls(os.listdir(), pand=1)

def amod():
    if len(os.listdir()) == 0:
        return ''
    num = list(range(len(os.listdir())))
    name = os.listdir()
    isdir = ['<DIR>' if os.path.isdir(i) else '<FILE>' for i in os.listdir()]
    timef = [str(time.ctime(os.path.getctime(i))) for i in os.listdir()]
    #inf =  [dict(os.lstat(i)) for i in os.listdir()]
    return splitzip(num, name, isdir, timef, #inf,
                    mods=[0, 0, 0, 0], pandp=[0, 0, 0, 0], pandl=[])
def lsdir(mod='n'):
    d = {'n': lambda: nmod(),
         'a': lambda: amod()
         }
    rez = d[mod]()
    print(rez)

