#include <bits/stdc++.h>
#include <iostream>

using namespace std;


#define MAX_SIZE 1000005
 
// from geeksforgeeks - https://www.geeksforgeeks.org/program-to-find-the-nth-prime-number/
void SieveOfEratosthenes(vector<int>& primes)
{
	// Create a boolean array "IsPrime[0..MAX_SIZE]" and
	// initialize all entries it as true. A value in
	// IsPrime[i] will finally be false if i is
	// Not a IsPrime, else true.
	bool IsPrime[MAX_SIZE];
	memset(IsPrime, true, sizeof(IsPrime));
 
	for (int p = 2; p * p < MAX_SIZE; p++) {
		// If IsPrime[p] is not changed, then it is a prime
		if (IsPrime[p] == true) {
			// Update all multiples of p greater than or
			// equal to the square of it
			// numbers which are multiple of p and are
			// less than p^2 are already been marked.
			for (int i = p * p; i < MAX_SIZE; i += p)
				IsPrime[i] = false;
		}
	}
 
	// Store all prime numbers
	for (int p = 2; p < MAX_SIZE; p++)
		if (IsPrime[p])
			primes.push_back(p);
}

int main() {
	vector<int> primes;
	SieveOfEratosthenes(primes);
	cout << "Result: " << primes[10000];
	return primes[10000];
}