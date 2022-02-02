require 'prime'

def main() 
	return Prime.each(2e6).to_enum.reduce(:+)
end

p main()