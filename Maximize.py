from itertools import product
def f(n):
    p = []
    for i in n:
        x = (i**2)
        p.append(x)
    return(p)

k = list(map(int,input().split()))
l = []
for i in range(k[0]):
    d = f(list(map(int,input().split()))[1:])
    l.append(d)

print(max(list(map(lambda x: sum(x)%k[1], list(product(*l))))))
