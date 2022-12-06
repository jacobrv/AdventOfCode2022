#with open('sample_input.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    
line = lines[0].strip()

def checkUnique(input) -> bool:
    inputSet = set([*input])
    uniqueList = list(inputSet)
    return uniqueList.__len__() == input.__len__()

for i in range(line.__len__()-13):
    testString = line[i:i+14]
    if(checkUnique(testString)):
        print(testString)
        print(i+14)
        break
