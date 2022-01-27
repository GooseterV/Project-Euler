function compute() {
	$a = 1;
	$b = 2;
	$total = 0;
	while ($a < 4000000) {
		if ($a % 2 == 0) {
			$total += $a;
		}
		$c = $a + $b;
		$a = $b;
		$b = $c;
	}
	return $total;
}
echo compute();