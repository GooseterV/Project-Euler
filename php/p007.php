<?php
function generatePrimes($MAX_SIZE){
	$primes = [];
	$IsPrime = array_fill(0, $MAX_SIZE, TRUE);
	for ($p = 2; $p * $p < $MAX_SIZE; $p++) {
		if ($IsPrime[$p] == 1) {
			for ($i = $p * $p; $i < $MAX_SIZE; $i += $p) {
				$IsPrime[$i] = FALSE;
			}
		}
	}
 
	for ($p = 2; $p < $MAX_SIZE; $p++) {
		if ($IsPrime[$p] == 1) {
			array_push($primes, $p);
		}

	}
	return $primes;
}


function main() {

	$p = generatePrimes(1000000);
	return $p[10000];
};

echo main();
?>