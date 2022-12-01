#with open('sample_input.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()


elves = []
bags = []

for line in lines:
    line = line.strip()
    if(line == ''):
        elves.append(bags.copy())
        bags = []
    else:
        bags.append(line)

if(bags.__len__() > 0):
    elves.append(bags.copy())
    bags = []


#print(elves)

highIndex = -1
highTotal = -1

for idx, elf in enumerate(elves):
    total = 0
    for bag in elf:
        total = total + int(bag)
    if(total > highTotal):
        highTotal = total
        highIndex = idx
        
print(highIndex)
print(highTotal)