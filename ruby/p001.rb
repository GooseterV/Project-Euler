def main()
	total = 0
	for i in 1..1000 do
		if i % 3 == 0 || i % 5 == 0 then
			total += i
		end
	end
	return total
end
puts main()