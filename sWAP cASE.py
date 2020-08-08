def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# k = ([i.lower() if i.isupper() else i.upper() for i in input()])
# print(''.join(k))
# k = input()
# for i in k:
#     if i.isupper():
#         k = i.lower()
#     else:
#         k = i.upper()
#     print("".join(k),end='')

