l = []
for i in range(int(input())):
    l.append(int(input()))
d = []
for p in l:
    for s in l:
        if abs(p-s)==1:
            s = d.append(map(a+b,(l.count(p),l.count(s))))
try:
    print(min(d))
except:
    print(1)