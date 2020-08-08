def maximumPerimeterTriangle(a):
    l = []
    for i in range(len(a)):
        try:
            if a[i] + a[i+1] > a[i+2]:
                l.append((a[i],a[i+1],a[i+2]))
        except:
            continue
    if len(l) == 0:
        return('-1')
    else:
        return(max(l))

a = [1,2,3,4,5,10]
print(maximumPerimeterTriangle(sorted(a)))
