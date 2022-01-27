#include <iostream>
using namespace std;

int main() {
	int total = 0;
	int a = 1;
	int b = 2;
	while (a <= 4000000) {
		if (a % 2 == 0) {
			total += a;
		};
		int c = a + b;
		a = b;
		b = c;
	};
	cout << total;
	return total;
};

