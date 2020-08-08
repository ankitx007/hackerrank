from random import *
Guess = ''
password = input('Password: ')
letters = []
alpha = 'a'
for i in range(26):
    letters.append(alpha)
    alpha = chr(ord(alpha)+1)
i = 0
while(Guess!= password):
    Guess =''
    for letter in password:
        guessletter = letters[randint(0,25)]
        Guess = str(guessletter) + str(Guess)
        i+=1
        print('Password Cracked', Guess,'took', i,'trials.')