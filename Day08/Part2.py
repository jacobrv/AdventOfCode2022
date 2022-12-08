#with open('sample_input.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()

trees = []

for line in lines:
    tLine = line.strip()
    aLine = [*tLine]
    for c in range(0,len(aLine)):
        aLine[c] = int(aLine[c])
    trees.append(aLine)

def numVisibleToLeft(x,y) -> int:
    #print(f'Looking Left From: ({x},{y})')
    if y == 0:
        #print('NumVis: 0')
        return 0
    numVis = 0
    for i in reversed(range(0,y)):
        #print(f'Checking: ({x},{i})')
        if trees[x][i] < trees[x][y]:
            numVis += 1
        else:
            numVis += 1
            break
    #print(f'NumVis: {numVis}')
    return numVis

def numVisibleToRight(x,y) -> int:
    #print(f'Looking Right From: ({x},{y})')
    if y == len(trees[0]):
        return 0
    numVis = 0
    for i in range(y+1,len(trees[0])):
        #print(f'Checking: ({x},{i})')
        if trees[x][i] < trees[x][y]:
            numVis += 1
        else:
            numVis += 1
            break
    #print(f'NumVis: {numVis}')
    return numVis

def numVisibleToTop(x,y) -> int:
    #print(f'Looking Up From: ({x},{y})')
    if x == 0:
        return 0
    numVis = 0
    for i in reversed(range(0,x)):
        #print(f'Checking: ({i},{y})')
        if trees[i][y] < trees[x][y]:
            numVis += 1
        else:
            numVis += 1
            break
    #print(f'NumVis: {numVis}')
    return numVis

def numVisibleToBottom(x,y) -> int:
    #print(f'Looking Down From: ({x},{y})')
    if x == len(trees):
        return 0
    numVis = 0
    for i in range(x+1,len(trees)):
        #print(f'Checking: ({i},{y})')
        if trees[i][y] < trees[x][y]:
            numVis += 1
        else:
            numVis += 1
            break
    #print(f'NumVis: {numVis}')
    return numVis

def numVisibleAtAll(x,y) -> int:
    #print('')
    #print(f'##### ({x},{y}) #####')
    #print('')
    numVisible = 1
    numVisible *= numVisibleToLeft(x,y)
    numVisible *= numVisibleToRight(x,y)
    numVisible *= numVisibleToTop(x,y)
    numVisible *= numVisibleToBottom(x,y)
    #print(f'TotalNumVis: {numVisible}')
    return numVisible

scenicScores = []
vMap = []

for x in range(0,len(trees)):
    vMap.append([])
    for y in range(0,len(trees[0])):
        vScore = numVisibleAtAll(x,y)
        vMap[x].append(vScore)
        scenicScores.append(vScore)

for tree in trees:
    print(tree)
    
print('======')

for m in vMap:
    print(m)

scenicScores.sort()
scenicScores.reverse()
print('***')
print(scenicScores[0])
print('***')