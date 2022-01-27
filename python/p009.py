import math

def compute():
    for a in range(1, 1001):
        for b in range(1, 1001):
            for c in range(1, 1001):
                abc = [a,b,c]
                if a + b + c == 100 and a ** 2 + b ** 2 == c ** 2:
                    return math.prod(abc)
print(compute())