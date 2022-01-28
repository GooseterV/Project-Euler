function smallestFactor(x) 
	for i = 2, math.floor(math.pow(x, 0.5)), 1 do
		if x % i == 0 then
			return i
		end
	end
	return x  
end

function main() 
	x = 600851475143
	while true do
		y = smallestFactor(x)
		if y < x then
			x = x / y
		else 
			return x
		end
	end
end
print(main())