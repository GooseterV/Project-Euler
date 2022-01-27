function isPalendromic(n) {
	let nray = Array.from(
		String(n), (i) => (Number(i))
	);
	let reversed = nray.reverse();
	
	
	return String(n) === reversed.join("");
};

function main() {
	let n = [];
	for (let i = 100; i < 1000; i++ ) {
		for (let j = 100; j < 1000; j++) {
			let k = i * j;
			if (isPalendromic(k)) {
				n.push(k);
			};
		};
	};
	return Math.max(n);
};
console.log(main());
