f = open("input.txt", "r")
input = f.read()

inputArray = input.split('\n')

points = 0
listPriorities = []

for rucksac in inputArray:
    holder = ''
    for x in range(len(rucksac)//2):
        for y in range(len(rucksac)//2, len(rucksac)):
            if rucksac[x] == rucksac[y]:
                holder = rucksac[x]
    listPriorities.append(holder)
                
for priority in listPriorities:
    if priority.isupper():
        points += ord(priority) - 38
    else:
        points += ord(priority) - 96

print(points)

        
