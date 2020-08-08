def journeyToMoon(n, astronaut):
    l =[]
    for i in range(n):
        l.append(i)
    for j in range(len(astronaut)):
        if astronaut[j][0] in l:
            l.remove(astronaut[j][0])
        if astronaut[j][0] in l:
            l.remove(astronaut[j][0])
    print(merge(astronaut))


def merge(lsts):
    sets = [set(lst) for lst in lsts if lst]
    merged = True
    while merged:
        merged = False
        results = []
        while sets:
            common, rest = sets[0], sets[1:]
            sets = []
            for x in rest:
                if x.isdisjoint(common):
                    sets.append(x)
                else:
                    merged = True
                    common |= x
            results.append(common)
        sets = results
    return sets


astronaut= [[0,1],
      [2,3],
      [0,4]]
n = 5
journeyToMoon(n, astronaut)