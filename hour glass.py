s = []
a=[]
n = int(input())
for i in range(n):
    k = list(map(int, input().split()))
    a.append(k)
for i in range(4):
    for j in range(4):
        try:
            k = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2]
            s.append(k)
        except:
            continue
print(max(s))