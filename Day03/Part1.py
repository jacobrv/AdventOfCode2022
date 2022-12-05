#with open('sample_input.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
        for i in range(wanted_parts) ]



bags = []

for line in lines:
    line = line.strip()
    if(line == ''):
        pass
    else:
        bags.append(split_list([*line], 2))

total = 0

for bag in bags:
    for item in bag[0]:
        if item not in bag[1]:
            pass
        else:
            if item.isupper():
                #print(ord(item)-38)
                total = total + ord(item)-38
            else:
                #print(ord(item)-96)
                total = total + ord(item)-96
            #print(item)
            break
    #print(bag)

print(total)