f = open("input.txt", "r")
input = f.read()

inputArray = input.split('\n')

points = 0
listPriorities = []

for i in range(0, len(inputArray), 3):
    holder = ''
    for char in inputArray[i]:
        if char in inputArray[i+1] and char in inputArray[i+2]:
            holder = char
    listPriorities.append(holder)
            
for priority in listPriorities:
    if priority.isupper():
        points += ord(priority) - 38
    else:
        points += ord(priority) - 96

print(points)

        
