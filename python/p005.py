from math import gcd, prod

def main():
	count = 1
	for i in range(1, 21):
		count *= i // gcd(i, count)
	return count