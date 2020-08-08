s = input()
k = sorted(''.join(filter(lambda i:i.isdigit(), s)))
l = sorted(''.join(filter(lambda i:i.isupper(), s)))
m = sorted(''.join(filter(lambda i:i.islower(), s)))
d=''
for i in range(len(m)):
        d += d.join(m[i])
print(d,end='')
f=''
for i in range(len(l)):
        f += f.join(l[i])
print(f,end='')
g,e,o='','',''
for i in range(len(k)):
    if int(k[i])%2==0:
        e+=e.join(k[i])
    else:
        o+=o.join(k[i])

print(o,e,sep='')