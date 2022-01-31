def isPalendromic(n)
	s = n.to_s()
	return s == s.reverse()
end

def main() 
	palendromes = []
	for i in 100..1000 do
		for j in 100..1000 do
			prod = j * i 
			if isPalendromic(prod) then
				palendromes.append(prod)
			end
		end
	end
	return palendromes.max()
end

puts main()