f = open("input.txt", "r")
input = f.read()

elves = []

array = input.split('\n\n')
for elf in array:
    elves.append(elf.splitlines())

allCal = []

for elf in elves:
    holder = 0
    for item in elf:
        holder += int(item)
    allCal.append(holder)
    
result = sorted(allCal,reverse=True)

print(result[0])
print(result[0] + result[1] + result[2])