with open("classmates", mode="w+", encoding='utf-8') as f:
    f.write('''hi
123
321
456
123''')
    f.seek(0, 0)
    k = f.readlines()
    for i in range(len(k)):
        line = k[i].split(' ')
