
def compute():
    return (sum([j for j in range(1, 101)])**2) - sum([i**2 for i in range(1, 101)])
print(compute())