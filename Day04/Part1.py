#with open('sample_input.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    

bags = []

for line in lines:
    line = line.strip()
    if(line == ''):
        pass
    else:
        pair = line.split(',')
        s1 = pair[0].split('-')
        s2 = pair[1].split('-')
        bags.append([s1, s2])
        
print(bags)

numContained = 0

for bag in bags:
    if(int(bag[0][0]) >= int(bag[1][0]) and int(bag[0][1]) <= int(bag[1][1])):
        numContained += 1
        print(bag)
        continue

    if(int(bag[1][0]) >= int(bag[0][0]) and int(bag[1][1]) <= int(bag[0][1])):
        numContained += 1
        print(bag)
        continue
    
print(numContained)