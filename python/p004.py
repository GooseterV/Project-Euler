def calculate():
    l = []
    for x in range(100, 1000):
        for y in range(100, 1000):
            s = str(x*y)
            ss = []
            for c in range(len(s), 0, -1):
                ss.append(s[c-1])
            #print(list(s), ss)
            if list(s) == list(ss):
                l.append(x*y)
    return max(l)
print(calculate())