from itertools import *
s, n = input().split()
print(*[''.join(j) for j in combinations_with_replacement(sorted(s),int(n))],sep='\n')