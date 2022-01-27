from funcs import factors, isPrime

def compute():
    return max([i for i in factors(600851475143) if  isPrime(i)])
print(compute())
