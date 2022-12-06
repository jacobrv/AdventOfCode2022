#with open('sample_input.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    
line = lines[0].strip()

def checkUnique(input) -> bool:
    inputSet = set([*input])
    uniqueList = list(inputSet)
    return uniqueList.__len__() == input.__len__()

for i in range(line.__len__()-3):
    testString = line[i] + line[i+1] + line[i+2] + line[i+3]
    if(checkUnique(testString)):
        print(testString)
        print(i+4)
        break