#with open('sample_input.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    

stacks = []
rows = []


def printStacks():
    print('***')
    for stack in stacks:
        print(stack)

for line in lines:
    #line = line.strip()
    if(line == '\n'):
        break
    else:
        cols = []
        parsedLine = [*line]
        start = 0
        end = len(parsedLine)
        step = 4
        for i in range(start, end, step):
            x = i
            cols.append(parsedLine[x:x+step][1])
        #print(cols)
        rows.append(cols)
        
rows.reverse()

for i in range(10):
    stacks.append([])

for row in rows:
    print(row)
    if(row[0]=='1'):
        continue
    slot = 1
    for item in row:
        if(item!=' '):
            stacks[slot].append(item)
        slot += 1
        
printStacks()

instructions = []

for line in lines:
    #line = line.strip()
    if('move' in line):
        slots = line.strip().split(' ')
        instructions.append([int(slots[1]), int(slots[3]), int(slots[5])])

#print(instructions)

for inst in instructions:
    fromStack = inst[1]
    toStack = inst[2]
    tempStack = []
    for i in range(inst[0]):
        popped = stacks[fromStack].pop()
        tempStack.append(popped)
    tempStack.reverse()
    for temp in tempStack:
        stacks[toStack].append(temp)
        
        
printStacks()

message = ''

for stack in stacks:
    if(stack.__len__()>0):
        message = message + stack[stack.__len__()-1]
        
print(message)