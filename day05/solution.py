f = open("input.txt", "r")
input = f.read()

inputArray = input.split('\n\n')

stacks = inputArray[0].split('\n')
moves = inputArray[1].split('\n')
temp = []

for i, line in enumerate(moves):
    moves[i] = line.replace('move ', '').replace(' from ', '-').replace(' to ', '-').split('-')
    
for line in moves:
    for i, char in enumerate(line):
        line[i] = int(line[i])

for i, line in enumerate(stacks):
    for j in range(1, len(line), 4):
        temp.append(line[j])

new = []
for i in range(1,10):
    new.append([])

i = 0
while i < 9:
    for j in range(0,9):
        new[i].append(temp[i + j * 9])
    i += 1

for i, list in enumerate(new):
    new[i].reverse()

for i in range(0, 9):
    while new[i][len(new[i])-1] == ' ':
        new[i].pop()

new.insert(0,[])

for i, line in enumerate(moves):
    holder = []
    number = line[0]
    from_ = line[1]
    to_ = line[2]
    for j in range(0, number):
        brick = new[from_].pop()
        holder.append(brick)
    # for first part no reverse
    holder.reverse() 
    new[to_] += holder

result = ''
for x in range (1, 10):
    result += new[x][len(new[x])-1]

print(result)    