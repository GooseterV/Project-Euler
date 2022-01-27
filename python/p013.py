


def compute():
    l = []
    for i in range(1, 100000):
        ll = []
        n = i
        ll.append(n)
        if n % 2 == 0:
            n //= 2
        elif n % 2 != 0:
            n *= 3 
            n += 1
        
        if n == 1:
            return
    
        