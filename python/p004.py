from funcs import isPalendromic

def main():
    # shorthand for
    # palendromes = []
    # for i in range(100, 1000):
    #   for j in range(100, 1000):
    #      prod = i * j
    #      if isPalendromic(prod):
    #           palendromes.append(prod)
    #  print(max(palendromes))
    return max(i * j for i in range(100, 1000) for j in range(100, 1000) if isPalendromic(i*j))
print(main())