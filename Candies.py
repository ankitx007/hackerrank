n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
p =[1]
for j in range(len(l)):
    try:
        if l[j+1]>l[j]:
            p.append(p[j]+1)
        else:
            p.append(1)
    except:
        continue
print(sum(p))
