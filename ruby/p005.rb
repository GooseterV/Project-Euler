def gcd(a, b) 
	while b != 0 do
		c = a % b
		a = b
		b = c
	end
	return a
end

def main() 
	count = 1
	for i in 1..20 do
		count = count * (i / gcd(i, count).floor())
	end
	return count

end

puts main()