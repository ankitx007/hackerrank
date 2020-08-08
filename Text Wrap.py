s,l = int(input('Enter a the range:\n\t Enter the starting point: ')), int(input('\t Enter the end point: '))
e = 0
o = 0
for i in range(s,l+1):
    for k in range(2,(i//2)):
        if i%k==0:
            print(i,'is not a prime number as it is divisble by', k, end='.\n')
            e+=1
            break
    else:
        print(i,'is a Prime number.')
        o+=1

print('\n',e,'is the total no. of Non Primes.')
print(' ',o,'is the total no. of Primes.')