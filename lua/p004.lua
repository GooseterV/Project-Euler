function isPalendromic(n)
	s = tostring(n)
	return s == string.reverse(s)
end
  
function main() 
	palendromes = {}
	for i = 100, 1000, 1 do
		for j = 100, 1000, 1 do
			prod = j * i 
			if isPalendromic(prod) then
				table.insert(palendromes, prod)
			end
		end
	end
	return math.max(unpack(palendromes))
end

print(main())

