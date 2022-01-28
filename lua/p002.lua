
function main() 
	total = 0
	a = 1
	b = 1
	while a <= 4000000 do
		if a % 2 == 0 then
			total = total + a
		end
		c = a + b
		a = b
		b = c
	end
	return total
end

print(main())

