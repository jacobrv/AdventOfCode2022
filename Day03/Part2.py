#with open('sample_input.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
        for i in range(wanted_parts) ]



groups = []
bags = []
groupCount = 0

for line in lines:
    line = line.strip()
    if(line == ''):
        pass
    else:
        bags.append([*line])
        groupCount = groupCount + 1
        if groupCount >= 3:
            groupCount = 0
            groups.append(bags)
            bags = []

total = 0

for group in groups:
    print('**************')
    for bag in group:
        print(bag)
    for item in group[0]:
        if item in group[1]:
            if item in group[2]:
                if item.isupper():
                    total = total + ord(item)-38
                    print(item)
                    break
                else:
                    total = total + ord(item)-96
                    print(item)
                    break

print(total)
