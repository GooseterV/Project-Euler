
#include <string>
#include <algorithm>
#include <list>
#include <iostream>

using namespace std;

bool isPalendromic(int n) {
	string s = to_string(n);
	string c = to_string(n);
	reverse(c.begin(), c.end());
	return c == s;
}

int main() {
	list<int> palendromes = {};
	for (int i = 100; i < 1000; i++) {
		for (int j = 100; j < 1000; j++) {
			int prod = i * j;
			if( isPalendromic(prod) ) {
				palendromes.push_back(prod);
			}
		}
	}
	palendromes.sort();
	int parr[palendromes.size()];
	copy(palendromes.begin(), palendromes.end(), parr);
	return parr[palendromes.size()-1];
}