function gcd(a, b) 
	while b ~= 0 do
		c = a % b
		a = b
		b = c
	end
	return a
end

function main() 
	count = 1
	for i = 1, 20, 1 do
		count = count * math.floor(i / gcd(i, count))
	end
	return count

end

print(main())