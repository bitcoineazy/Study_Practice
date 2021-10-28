import os
Path_of_project = [os.path.normpath(os.getcwd())]
Work_path = ["None"]
def get_work_path(name):
    with open('Setting.txt', 'r', encoding="utf-8") as f:
        for i in f.readlines():
            s = i.split()
            if name == s[0]:
                Work_path[0] = os.path.normpath(s[1])
                return Work_path[0]

Mod_out=[False]