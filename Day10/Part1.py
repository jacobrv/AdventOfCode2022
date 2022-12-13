#with open('sample_input.txt', 'r') as f:
#with open('sample_input copy.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()

instMaxCycleTime = 3

instructions = []

for line in lines:
    tLine = line.strip()
    if tLine == 'noop':
        instructions.append([tLine, '0'])
    else:    
        aLine = tLine.split(' ')
        aLine[1] = int(aLine[1])
        instructions.append(aLine)    

regAtT = [1]
reg = 1
queuedAdds = [0]*instMaxCycleTime
currentCycle = 0

def dequeueAdd() -> int:
    addToReturn = queuedAdds[0]
    for i in range(instMaxCycleTime-1):
        queuedAdds[i] = queuedAdds[i+1]
    queuedAdds[instMaxCycleTime-1] = 0
    return addToReturn
    
def enqueueAdd(num, cycleTime):
    queuedAdds[cycleTime] += num
    
    
for inst in instructions:
    if inst[0] == 'noop':
        enqueueAdd( 0, 1)
        
        n = dequeueAdd()
        reg += n
        currentCycle += 1
        regAtT.append(reg)
        
        print(queuedAdds)
        print(reg)
        
    if inst[0] == 'addx':
        enqueueAdd( inst[1], 1)
        enqueueAdd( 0, 1)
        
        n = dequeueAdd()
        reg += n
        currentCycle += 1
        regAtT.append(reg)
        
        print(queuedAdds)
        print(reg)
        
        n = dequeueAdd()
        reg += n
        currentCycle += 1
        regAtT.append(reg)
        
        print(queuedAdds)
        print(reg)
    
print('*')
print(regAtT[139])
print(regAtT[140])
print(regAtT[141])
print('*')
print(regAtT[179])
print(regAtT[180])
print(regAtT[181])
print('*')
print(regAtT[219])
print(regAtT[220])
print(regAtT[221])
print('*')

total = 0

for i in range(20, 221, 40):
    print('#')
    print(i)
    print(regAtT[i-1])
    total += (i * regAtT[i-1])
    
print(total)
print(len(regAtT))


