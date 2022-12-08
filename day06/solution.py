f = open("input.txt", "r")
input = f.read()

inputArray = input.split()

datastream = list(input)

numbers = []

for i in range(0, len(datastream) - 4):
    if datastream[i] not in datastream[i+1: i+4] and datastream[i+1] not in datastream[i+2: i+4] and datastream[i+2] is not datastream[i+3]:
        print(i+4)
        break

for i in range(0, len(datastream) - 14):
    if len(set(datastream[i: i + 14])) == 14:
        print (i+14)
        break