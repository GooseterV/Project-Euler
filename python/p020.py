import math
def compute():
    return sum([int(j) for j in str(math.prod([i for i in range(101, 0, -1)]))])

print(compute())