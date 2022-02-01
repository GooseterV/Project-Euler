def main() 
	total = 0
	total2 = 0
	for i in 1..100 do
		total += i**2
		total2 += i
	end
	return (total2**2) - total
end

puts main()