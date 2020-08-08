# n =int(input())
# for i in range(1, n+1):
#     print(str(i).rjust(2,' '), str(oct(i)[2:]).rjust(2,' '), str(hex(i)[2:]).upper().rjust(2, ' '), str(bin(i)[2:]).rjust(5, ' '))

def print_formatted(k):
    width = len("{0:b}".format(k))
    for i in range(1, n + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)