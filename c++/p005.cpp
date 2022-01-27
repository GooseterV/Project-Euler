#include <string>
#include <algorithm>
#include <list>
#include <iostream>
#include <math.h>  

using namespace std;

int gcd(int a, int b) {
	while (b != 0) {
		int c = a % b;
		a = b;
		b = c;
	}
	return a;
}

int main() {
	int count = 1;
	for (int i = 1; i < 21; i++) {
		count *= floor(i / gcd(i, count));
	}
	cout << "Result: \n";
	cout << count;
	return count;
}