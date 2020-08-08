for i in range(int(input())):
    p = input()
    if p == '0':
        print(False)
        continue
    try:
        float(p)
        print(True)
    except:
        print(False)