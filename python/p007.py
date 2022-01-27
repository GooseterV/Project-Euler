from funcs import is_prime
def compute():
    j = []
    c = 2
    while len(j) < 10001:
        if is_prime(c):
            j.append(c)
        c += 1
    return j[10000]
print(compute())