def compareTriplets(a, b):
    sa = 0
    sb = 0
    for i in range(3):
        if a[i]>b[i]:
            sa+=1
        elif b[i]>a[i]:
            sb+=1
    return([sa,sb])


a = [17, 28, 30]
b = [99, 16, 8]
print(compareTriplets(a, b))