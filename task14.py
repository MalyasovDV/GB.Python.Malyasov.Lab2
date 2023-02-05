def listOfDegrees(top):
    a = 1
    degrees = []
    while(a < top):
        degrees.append(a)
        a *= 2
    return degrees

print("Type")
top = int(input())

print(listOfDegrees(top))

