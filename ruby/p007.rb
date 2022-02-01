require 'prime'

def nthprime(n) 
	Prime.take(n).last
end

def main() 
	return nthprime(10001)
end
puts main()