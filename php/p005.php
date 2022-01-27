function gcd($a, $b) {
	while ($b != 0) {
		$c = $a % $b;
		$a = $b;
		$b = $c;
	}
	return $a;
}

function main() {
	$count = 1;
	for ($i = 1; $i <= 20; $i++) {
		$count *= floor($i / gcd($i, $count));
	}
	return $count;
}
echo main();