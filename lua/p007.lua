function sieve_of_eratosthenes(n)
	local is_prime = {}
	local max = 100050
	for i = 0, max-1 do
		is_prime[i] = 1 ~= i
	end
	
	for i = 1, math.floor(math.sqrt(max)) do
		if is_prime[i] then
			for j = i*i, max, i do
				is_prime[j] = false
			end
		end
	end
	primes = {}
	for p = 0, max do
		if is_prime[p] == true then
			table.insert(primes, p)
		end
	end
	return primes[n-1]
end

function main()
	return sieve_of_eratosthenes(10001)
end

print(main())