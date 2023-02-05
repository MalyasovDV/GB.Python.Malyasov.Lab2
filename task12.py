from math import sqrt

def findDivisors(composition):
    listOfDivisors = []
    for potentialDivisor in range(1, int(sqrt(composition) + 1)):
        if (composition % potentialDivisor == 0):
            listOfDivisors.append(potentialDivisor)
    return listOfDivisors

def findNumbers(listOfDivisors, sum, composition):
    for divisor in listOfDivisors:
        if (divisor + composition/divisor == sum):
            print(f"первое число - {divisor} \nвторое число - {composition//divisor}")
            break


print("Type sum of these numbers")
sum = int(input())
print("Type composition of these numbers")
composition = int(input())

findNumbers(findDivisors(composition), sum, composition)


