p = input().split()
n = int(input())
a = sum(list(map(int, input().split())))/n
print('Name:',p[1],end=', ')
print(p[0])
print('ID:',p[2])
if a>=90 and a<=100:
    print('Grade: O')
elif a>=80 and a<=90:
    print('Grade: E')
elif a>=70 and a<=80:
    print('Grade: A')
elif a>=55 and a<=70:
    print('Grade: P')
elif a>=40 and a<=55:
    print('Grade: D')
else:
    print('Grade: T')