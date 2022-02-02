from functools import reduce

def main():
    return sum(list(int(j) for j in str(reduce(lambda x, y: x*y, range(1, 101)))))

print(main())