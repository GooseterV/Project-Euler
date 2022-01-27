import math

def compute():
	count = 1
	for i in range(1, 21):
		count *= math.floor(i / math.gcd(i, count))
	return count

print(compute())