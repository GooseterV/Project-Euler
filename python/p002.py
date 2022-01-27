from funcs import is_prime

def calculate():
	fseq = [1, 1]
	count = 0
	while fseq[len(fseq)-1] <= 4000000:
		fseq.append(fseq[count]+fseq[count+1])
		count += 1
	return sum(i for i in fseq if is_prime(i))
print(calculate())