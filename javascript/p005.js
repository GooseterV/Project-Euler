function gcd(a, b) {
	while (b != 0) {
		c = a % b;
		a = b;
		b = c;
	}
	return a;
}

function main() {
	let count = 1;
	for (let j = 1; j <= 20; j++) {
		count *= Math.floor(i / gcd(i, count));
	};
	return count;
};
console.log(main());