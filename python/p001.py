def main():
	# shorthand for
	# total = 0
	# for i in range(0, 1001):
	#	if i % 3 == 0 || i % 5 == 0:
	#		total += 1
	# print(total)
	return sum(i for i in range(0, 1001) if i % 3 == 0 or i % 5 == 0)
print(main())