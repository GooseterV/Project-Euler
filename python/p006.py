def main():
    # shorthand for
    # total1, total2 = 0, 0
    # for i in range(0, 101):
    #   total1 += i**2
    #   total2 += i
    # print(
    #   total1 - (total2**2)
    # )
    return (sum(i for i in range(0, 101))**2) - sum(i**2 for i in range(0, 101)) 

print(main())