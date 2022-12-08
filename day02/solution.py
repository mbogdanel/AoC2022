import copy
f = open("input.txt", "r")
input = f.read()

inputList = input.split('\n')
games = []

for ele in inputList:
    games.append(ele.split(' '))

games2 = copy.deepcopy(games)  

for game in games2:
    if game[1] == 'Y':
        game[1] = chr(ord(game[0]) + 23)
    elif game[1] == 'X':
        if game[0] == 'A':
            game[1] = 'Z'
        if game[0] == 'B':
            game[1] = 'X'
        if game[0] == 'C':
            game[1] = 'Y'
    elif game[1] == 'Z':
        if game[0] == 'A':
            game[1] = 'Y'
        if game[0] == 'B':
            game[1] = 'Z'
        if game[0] == 'C':
            game[1] = 'X'

def calcPoints(games):
    points = 0  
    for game in games:
        if ord(game[1]) - ord(game[0]) == 23:
            points += 3 + ord(game[1]) - 87
        else:
            if game[1] == 'X':
                if game[0] == 'B':
                    points += ord(game[1]) - 87
                else:
                    points += 6 + ord(game[1]) - 87
            if game[1] == 'Y':
                if game[0] == 'A':
                    points += 6 + ord(game[1]) - 87
                else:
                    points += ord(game[1]) - 87
            if game[1] == 'Z':
                if game[0] == 'A':
                    points += ord(game[1]) - 87
                else:
                    points += 6 + ord(game[1]) - 87
    return points

print(calcPoints(games))
print(calcPoints(games2)) 
