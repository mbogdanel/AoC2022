f = open("input.txt", "r")
input = f.read()

inputArray = input.split('\n')

assignments = []
pairs = 0
pairs2 = 0

for line in inputArray:
    assignments.append(line.replace(",", "-" ).split('-'))

for assignment in assignments:
    for i, ele in enumerate(assignment):
        assignment[i] = int(ele)

for ass in assignments:
    if (ass[0] >= ass[2] and ass[1] <= ass[3]) or (ass[2] >= ass[0] and ass[3] <= ass[1]):
        pairs += 1

for ass in assignments:
    if ass[0] in range(ass[2], ass[3]+1) or ass[1] in range(ass[2], ass[3]+1) or ass[2] in range(ass[0], ass[1]+1) or ass[3] in range(ass[0], ass[1]+1):
        pairs2 += 1        

print(pairs)    
print(pairs2)    

        
