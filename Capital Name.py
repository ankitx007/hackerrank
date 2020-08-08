# for i in range(len(s)):
#     if i==0:
#         print(''.join(s[i].upper()),end='')
#     elif s[i-1]==' ':
#         print(''.join(s[i].upper()),end='')
#     else:
#         print(''.join(s[i]),end='')
# def solve(s):
#     for k in range(len(s)):
#         if s[k]==' ' and s[k+1]!=' ':
#             l=k
#         elif s[k]==' ' and s[k+1]==' ':
#             if s[k]==' ' and s[k+1]==' ' and s[k+2]==' ':
#                 l=k+2
#                 break
#             else:
#                 l = k+1
#                 break
#         else:
#             pass
#     return(s[0].upper()+ ''.join(s[1:l+1])+ ''.join(s[l+1:l+2].upper())+ ''.join(s[l+2:]))

def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return(s)

s = input()
print(solve(s))


