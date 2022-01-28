#include <iostream>
#include <cmath>

using namespace std;

int smallestFactor(long x) {
	for (int i = 2; i <= floor(pow(x, 0.5)); i++) {
		if (x % i == 0) {
			return i;
		};
	};
	return x;  
};

int main() {
	long x = 600851475143;
	while (true) {
		int y = smallestFactor(x);
		if (y < x) {
			x /= y;
		} else {
			cout << "Result: " << x;
			return x;
		}
	};
	cout << "Result: " << x;
	
};