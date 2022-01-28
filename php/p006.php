function main() {
	$total = 0;
	$total2 = 0;
	for ($i = 1; $i <= 100; $i++) {
		$total += pow($i, 2);
		$total2 += $i;
	}
	return (pow($total2, 2) - $total);
}

echo main();