
p = [[int(i) for i in input().split(" ")] for j in range(3)]
s = [[8,1,6,3,5,7,4,9,2],[8,3,4,1,5,9,6,7,2],[2,7,6,9,5,1,4,3,8],[2,9,4,7,5,3,6,1,8],[6,1,8,7,5,3,2,9,4],[6,7,2,1,5,9,8,3,4],[4,3,8,9,5,1,2,7,6],[4,9,2,3,5,7,8,1,6]]
#Print the minimum cost of converting 's' into a magic square
r=[]
for i in range(8):
    r.append(0)
    for j in range(9):
        r[i]+=abs(s[i][j]-p[int(j//3)][j%3])
print(min(r))