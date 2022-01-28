#include <algorithm>
#include <iostream>
#include <math.h>  

using namespace std;

int main() {
	int total = 0;
	int total2 = 0;
	for (int i = 1; i <= 100; i++) {
		total += pow(i, 2);
		total2 += i;
	};
	cout << "Result: " << (pow(total2, 2) - total);
	return (pow(total2, 2) - total);
};

