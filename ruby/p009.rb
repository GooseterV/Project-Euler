def main()
	for a in 1..1000 do
		for b in 1..1000 do
			c = 1000 - a - b
			if a**2 + b**2 == c**2 then
				return a * b * c
			end
		end
	end
end

puts main()