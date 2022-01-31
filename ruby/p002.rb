def main()
	a = 1
	b = 2
	total = 0
	while total <= 4e6 do 
		if a % 2 == 0 then
			total += a
		end
		c = a + b
		a = b
		b = c
	end
	return total
end
puts main()