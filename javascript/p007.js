function generatePrimes(primes, MAX_SIZE){
	let IsPrime = Array(MAX_SIZE).fill(true);
	 
	let p,i;
	for (p = 2; p * p < MAX_SIZE;p++) {
		if (IsPrime[p] == true) {
			for(i = p * p; i < MAX_SIZE; i += p)
				IsPrime[i] = false;
		}
	}
 
	for (p = 2; p < MAX_SIZE; p++)
		if (IsPrime[p])
			primes.push(p);
	return primes;
}


function main() {
	let p = [];
	generatePrimes(p, 1e6);
	return p[10000];
};

console.log(main());