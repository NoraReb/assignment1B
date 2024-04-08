"""
OrderOfNumbers
"""
# Provide your solution here
#while True:
#    n1 = int(input("Enter number 1: "))
#    n2 = int(input("Enter number 2: "))
#    n3 = int(input("Enter number 3: "))
#    if n1 > n2 and n2 > n3:
#        print("descending")
#    elif n1 < n2 and n2 < n3:
#        print("ascending")
#    else:
#        print("no specific order")
#        if n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0:
#            print("All numbers are even")
#        elif n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0:
#            print("All numbers are odd")


"""
SumUp
"""
# Provide your solution here
n1 = input("n1: ")
n2 = input("n2: ")

sum = int(n1) + int(n2)
print(sum)
print(int(n1))

#if n1 < n2:
#    n1 = input("n1: ")
#    while n1 != n2:
#        print(int(n1))
#        n1 += 1
        # nicht praktikabel

#neuer Versuch:
n1 = input("n1: ")
while n1 != n2:
    if n1 < n2:
        print(int(n1))
        n1 += 1

print(int(n2))


#if n1 <= 0 or n2 <= 0:
#    print("at least one number is smaller or equal to zero")
#else:
#    if n1 > 0 and n2 > 0 and n2 < n1:
#        print("Error")
