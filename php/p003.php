<?php
function smallestFactor($x) {
	for ($i = 2; $i <= floor(pow($x, 0.5)); $i++) {
		if ($x % $i == 0) {
			return $i;
		};
	};
	return $x;  
};

function main() {
	$x = 600851475143;
	while (true) {
		$y = smallestFactor($x);
		if ($y < $x) {
			$x /= $y;
		} else {
			return $x;
		}
	};
};
echo main();
?>