def fillList(sides, n):
    print("Type sides of these coins")
    for i in range(n):
        sides.append(input())

def countHeads(sides):
    count = 0
    for head in sides:
        if (head == '0'):
            continue
        count += 1
    return count

print("Type the amount of coins")
n = int(input())
sides = []

fillList(sides, n)
print(f"sides list:{sides}")

heads = countHeads(sides)
if (heads > n - heads):
    print(n - heads)
else:
    print(heads)
