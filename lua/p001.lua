
function main() 
	total = 0
	for i =1, 1000, 1 do
		if i % 3 == 0 or i % 5 == 0 then
			total = total + i
		end
	end
	return total
end

print(main())

