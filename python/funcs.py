import math
import decimal
import random
import numpy
import itertools
from functools import reduce

def distance(points:list):
	"""
	Checks the distance between two points on a graph
	Parameters:
		points:list - list of tuples formatted [(x1, y1), (x2, y2)]
	Returns:
		distance - the distance inbetween two points
	"""
	return math.sqrt((points[1][1] - points[0][1])**2 + (points[1][0] - points[0][0])**2)

def isPrime(n):
	"""
	Checks primality on a number

	Parameters:
		n:int - the number to check primality on
	Returns:
		True - if n == prime
		False - if n != prime
	"""
	return all(n % i != 0 for i in range(int(n**0.5)+1)[2:])

def factors(n):
	"""
	Lists the factors of a number

	Parameters:
		n:int - the number to list factors
	Returns:
		factors - a set of the factors of n
	"""
	return set(f for i in range(1, int(n**0.5)+1) if n % i == 0 for f in [i, n//i])

def isPalendromic(n):
	"""
	Checks whether a number is a palindrome (same backwards and forwards)

	Parameters:
		n:int - the number to check if palendromic
	Returns:
		True - if the number is a palendrome
		False - the latter
	"""
	return list(str(n))==list(reversed(list(str(n))))

def isPandigital(n, until=9):
	"""
	Checks whether a number is pandigital from 0 to `until` (contains each number from 0 to `until` in it's digits)

	Parameters:
		n:int - the number to check
		until:int - end value of range between 1 and 9
	Returns:
		True - if the number is pandigital with those parameters
		False - the latter
	"""
	return set(sorted(set(list(str(n))))) == set(sorted(set([str(i) for i in range(0, until+1)])))

# Credits to Project Nayuki
# 
# https://www.nayuki.io/page/project-euler-solutions
#
# https://github.com/nayuki/Project-Euler-solutions
#
# Functions `listPrimality`, `listPrimes`, and `nthPrime`

# Returns a list of True and False indicating whether each number is prime.
# For 0 <= i <= n, result[i] is True if i is a prime number, False otherwise.
def listPrimality(n):
	# Sieve of Eratosthenes
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(fsqrt(n) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result


# Returns all the prime numbers less than or equal to n, in ascending order.
# For example: listPrimes(97) = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ..., 83, 89, 97].
def listPrimes(n):
	return [i for (i, isprime) in enumerate(listPrimality(n)) if isprime]

def nthPrime(n):
	return next(itertools.islice(filter(isPrime, itertools.count(2)), n-1, None))


def nthRoot(num, root) -> float:
	"""
	Get the nth root of a number.
	Parameters:
		num : Number - the number you want to get the nth root of
		root : int - the root; 2 for the square root
	Returns:
		float - the nth root of num
	"""
	return num**(1./root)

def fsqrt(n) -> int:
	"""
	Get the floored square root of a number (`n`)
	Parameters:
		num : Number - the number you want to get floored sqrt of
	Returns:
		int - the nth root of num floored 
	"""
	return math.floor(nthRoot(n, 2))

def smallestPrimeFactor(n) -> int:
	for i in range(2, fsqrt(n) + 1):
		if n % i == 0:
			return i
	return n

def to_exponential(n, decimals_num:int=2) -> str:
	b = decimal.Decimal(str(decimal.Decimal(str(n)).copy_abs()))
	j = decimal.Decimal(math.floor(math.floor(b.log10())/3))
	h = round(decimal.Decimal(str(n))/10**(j*3), decimals_num)
	return decimal.Decimal(f"{h}e{math.floor(j)*3}")




