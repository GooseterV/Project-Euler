function main() 
	total = 0
	total2 = 0
	for i=1, 100, 1 do
		total = total + math.pow(i, 2)
		total2 = total2 + i
	end
	return (math.pow(total2, 2) - total)
end

print(main())