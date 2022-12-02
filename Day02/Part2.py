#with open('sample_input.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()

rounds = []

for line in lines:
    line = line.strip()
    if(line == ''):
        pass
    else:
        rounds.append(line)

print(rounds)

scoring = {
    "A": 1, 
    "B": 2,
    "C": 3,
    "L": 0,
    "T": 3,
    "W": 6
}

loses = {
    "B": "A",
    "C": "B",
    "A": "C",
}

beats = {
    "C": "A",
    "A": "B",
    "B": "C",
}

ties = {
    "A": "A",
    "B": "B",
    "C": "C",
}

grandTotal = 0

for round in rounds:
    result = ''
    pick = ''
    if(round[2] == 'X'):
        result = 'L'
        pick = loses[round[0]]
    if(round[2] == 'Y'):
        result = 'T'
        pick = ties[round[0]]
    if(round[2] == 'Z'):
        result = 'W'
        pick = beats[round[0]]
        
    roundTotal = scoring[result] + scoring[pick]
    print(roundTotal)
    grandTotal = grandTotal + roundTotal
    
    
print(grandTotal)