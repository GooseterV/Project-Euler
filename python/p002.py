from funcs import isPrime

def main():
	# previous fibonacci number, current fibonacci number
	x, y = 1, 2
	total = 0
	while x <= 4e6:
		# checking if x is even
		if x % 2 == 0:
			total += x
		z = x + y
		x = y
		y = z
	return total
print(main())