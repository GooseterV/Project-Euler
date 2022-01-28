function main() {
	let total = 0;
	let total2 = 0;
	for (let i = 1; i <= 100; i++) {
		total += i**2;
		total2 += i;
	};
	return ((total2**2) - total);
};

console.log(main());