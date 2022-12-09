#with open('sample_input.txt', 'r') as f:
#with open('sample_input_2.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()

ropes = []

for line in lines:
    tLine = line.strip()
    aLine = tLine.split(' ')
    aLine[1] = int(aLine[1])
    ropes.append(aLine)
    
for rope in ropes:
    print(rope)
    
positionsTailVisited = [[0,0]]

knots = [
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0]
]


def isTouching(head, tail):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1:
        return True
    return False


def checkAndAdjustTailPos(head, tail, i):
    if isTouching(head, tail):
        #print('T:0:0')
        return
    
    newPosition = [0,0]
    
    # inline but more than 1 away
    if head[0]==tail[0] and head[1]-tail[1] > 1:
        newPosition = [tail[0],tail[1]+1]
        #print('M:0:1')
    if head[0]==tail[0] and tail[1]-head[1] > 1:
        newPosition = [tail[0],tail[1]-1]
        #print('M:0:-1')
    if head[1]==tail[1] and head[0]-tail[0] > 1:
        newPosition = [tail[0]+1,tail[1]]
        #print('M:1:0')
    if head[1]==tail[1] and tail[0]-head[0] > 1:
        newPosition = [tail[0]-1,tail[1]]
        #print('M:-1:0')
    
    # not inline
    if head[0]!=tail[0] and head[1]!=tail[1]:
        if head[0] > tail[0]:
            newPosition[0] = tail[0] + 1
            #print('M:1:0')
        else:
            newPosition[0] = tail[0] - 1
            #print('M:-1:0')
        if head[1] > tail[1]:
            newPosition[1] = tail[1] + 1
            #print('M:0:1')
        else:
            newPosition[1] = tail[1] - 1
            #print('M:0:-1')
    
    if i == 8:
        matches = [x for x in positionsTailVisited if x[0] == newPosition[0] and x[1] == newPosition[1]]
        if len(matches) <= 0:
            positionsTailVisited.append(newPosition)
    tail[0] = newPosition[0]
    tail[1] = newPosition[1]
    return

def moveLeft(head, tail):
    head[0] -= 1
    for i in range(9):
        checkAndAdjustTailPos(knots[i], knots[i+1], i)
    return

def moveRight(head, tail):
    head[0] += 1
    for i in range(9):
        checkAndAdjustTailPos(knots[i], knots[i+1], i)
    return

def moveUp(head, tail):
    head[1] += 1
    for i in range(9):
        checkAndAdjustTailPos(knots[i], knots[i+1], i)
    return

def moveDown(head, tail):
    head[1] -= 1
    for i in range(9):
        checkAndAdjustTailPos(knots[i], knots[i+1], i)
    return

for rope in ropes:
    for i in range(int(rope[1])):
        #print(' ')
        #print('***')
        #print('Before')
        #print(f'Head: ({knots[0][0]},{knots[0][1]})')
        #print(f'Tail: ({knots[9][0]},{knots[9][1]})')
        #print('Moves')
        if rope[0] == 'L':
            moveLeft(knots[0], knots[1])
        if rope[0] == 'R':
            moveRight(knots[0], knots[1])
        if rope[0] == 'U':
            moveUp(knots[0], knots[1])
        if rope[0] == 'D':
            moveDown(knots[0], knots[1])
        #print('After')
        #print(f'Head: ({knots[0][0]},{knots[0][1]})')
        #print(f'Tail: ({knots[9][0]},{knots[9][1]})')

print(' ')
print('###')
#print(head)
#print(tail)
print('###')
for pos in positionsTailVisited:
    print(pos)
print('Total: '+str(len(positionsTailVisited)))