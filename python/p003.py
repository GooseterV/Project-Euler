from re import X
from funcs import smallestPrimeFactor

def main():
	x = 600851475143
	while True:
		y = smallestPrimeFactor(x)
		if y < x:
			x //= y
		else:
			return x
print(main())
