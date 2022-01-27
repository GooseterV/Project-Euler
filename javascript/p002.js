function main() {
	let total = 0;
	let a = 1;
	let b = 2;
	while (a <= 4000000) {
		if (a % 2 === 0) {
			total += a;
		};
		let c = a + b;
		a = b;
		b = c;
	};
	return total;
};

console.log(main());