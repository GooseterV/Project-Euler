def smallestFactor(x) 
	for i in 2..((x**0.5).floor()) do
		if x % i == 0 then
			return i
		end
	end
	return x  
end

def main() 
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
puts main()