#with open('sample_input.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()

trees = []

for line in lines:
    tLine = line.strip()
    aLine = [*tLine]
    trees.append(aLine)

for tree in trees:
    print(tree)

def isOnEdge(x,y) -> bool:
    if y == 0 or y == len(trees[0])-1:
        return True
    if x == 0 or x == len(trees)-1:
        return True
    return False

def isVisibleFromLeft(x,y) -> bool:
    if isOnEdge(x,y):
        return True
    vis = True
    for i in range(0,y):
        if trees[x][i] >= trees[x][y]:
            vis = False
    return vis

def isVisibleFromRight(x,y) -> bool:
    if isOnEdge(x,y):
        return True
    vis = True
    for i in range(y+1,len(trees[0])):
        if trees[x][i] >= trees[x][y]:
            vis = False
    return vis

def isVisibleFromTop(x,y) -> bool:
    if isOnEdge(x,y):
        return True
    vis = True
    for i in range(0,x):
        if trees[i][y] >= trees[x][y]:
            vis = False
    return vis

def isVisibleFromBottom(x,y) -> bool:
    if isOnEdge(x,y):
        return True
    vis = True
    for i in range(x+1,len(trees)):
        if trees[i][y] >= trees[x][y]:
            vis = False
    return vis

def isVisibleAtAll(x,y) -> bool:
    isVisible = False
    if isVisibleFromLeft(x,y):
        isVisible = True
    if isVisibleFromRight(x,y):
        isVisible = True
    if isVisibleFromTop(x,y):
        isVisible = True
    if isVisibleFromBottom(x,y):
        isVisible = True
    return isVisible

numVisible = 0

vMap = []

for y in range(0,len(trees)):
    vMap.append([])
    for x in range(0,len(trees[0])):
        vMap[y].append('.')
        if isVisibleAtAll(x,y):
            vMap[y][x] = 'V'
            numVisible += 1

for m in vMap:
    print(m)

print('***')
print(numVisible)
print('***')