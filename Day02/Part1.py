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
    "X": 1, 
    "Y": 2,
    "Z": 3,
    "L": 0,
    "T": 3,
    "W": 6
}

beats = {
    "X": "C",
    "Y": "A",
    "Z": "B",
}

ties = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}

grandTotal = 0

for round in rounds:
    result = 'L'
    if(beats[round[2]] == round[0]):
        result = 'W'
    if(ties[round[2]] == round[0]):
        result = 'T'
    roundTotal = scoring[result] + scoring[round[2]]
    print(roundTotal)
    grandTotal = grandTotal + roundTotal
    
    
print(grandTotal)