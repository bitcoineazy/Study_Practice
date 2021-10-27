import os
from math import ceil
from Sistem_var import *
from random import random
from functools import reduce


def check_path(path):
    work_path = Work_path[0]
    path = os.path.relpath(path, start=work_path)
    assert path[:2] != '..', "MYError: Выход вне рабочей директории"
    return path


def splitls(ls, pand=2, column=4):
    m = len(max(ls, key=len)) + pand
    ret = ''
    for i in range(ceil(len(ls) / column)):
        s = reduce(lambda x, y: x.ljust(m) + y.ljust(m), ls[i * column:i * column + column])
        ret += s + '\n'
    return ret[:-1]


def splitzip(*args, pandp=None, otherp=2, pandl=None, otherl=2, mods=None):
    for i in args:
        for j in range(len(i)):
            i[j] = str(i[j])

    if pandp is None:
        pandp = []

    if len(pandp) < len(args):
        for i in range(len(pandp), len(args)):
            pandp.append(otherp)

    if pandl is None:
        pandl = []

    if len(pandl) < len(args):
        for i in range(len(pandl), len(args)):
            pandl.append(otherl)

    pand = []
    for i_list, dop in zip(args, pandp):
        pand.append(len(max(i_list, key=len)))

    if mods is None:
        mods = []
    if len(mods) < len(args):
        for i in range(len(mods), len(args)):
            mods.append(1)

    ret = ''
    for lists in zip(*args):
        for numberlist in range(len(lists)):
            if mods[numberlist] == 0:
                r = lists[numberlist].rjust(pand[numberlist] + pandp[numberlist])
                r = ' ' * (pandl[numberlist]) + r
                ret += r
            else:
                r = lists[numberlist].ljust(pand[numberlist] + pandl[numberlist])
                r += ' ' * (pandp[numberlist])
                ret += r
        ret += '\n'
    return ret[:-1]
