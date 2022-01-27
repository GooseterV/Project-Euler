function isPalendromic($n) {
	$s = strval($n);
	$c = strrev($s);
	return $s == $c;
}

function compute() {
	$palendromes = array();
	for ($i = 100; $i < 1000; $i++) {
		for ($j = 100; $j < 1000; $j++) {
			$prod = $j * $i;
			if (isPalendromic($prod)) {
				array_push($palendromes, $prod);
			}
		}
	}
	return max($palendromes);
}
echo compute();