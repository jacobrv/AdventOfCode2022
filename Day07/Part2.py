import json

#with open('sample_input.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()

instructions = []

for line in lines:
    instructions.append(line.strip())

curDir = ['/']

class file:
    name: str
    size: int
    
class dir:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    name: str
    files: list
    folders: list
    size: int

dirStruct = dir()
dirStruct.name = 'root'
dirStruct.size = 0
dirStruct.files = []
dirStruct.folders = []


def addFile(dirName, fileName, size):
    tDir = dirStruct
    for dn in dirName:
        found = [x for x in tDir.folders if x.name == dn]
        
        if len(found)>0:
            tDir = found[0]
        else:
            nDir = dir()
            nDir.name = dn
            nDir.size = 0
            nDir.files = []
            nDir.folders = []
            tDir.folders.append(nDir)
            tDir = nDir
    nFile = file()
    nFile.name = fileName
    nFile.size = size
    tDir.files.append(nFile)
    
def printDirStruct(ds, indent):
    print(indent + '- ' + ds.name + ' (dir, size='+str(ds.size)+')')
    for f in ds.files:
        print(indent + '  - ' + f.name + ' (file, size='+str(f.size)+')')
    for d in ds.folders:
        printDirStruct(d, indent + '  ')

for idx, inst in enumerate(instructions):
    
    if(inst[0]!='$'):
        continue

    if(inst[0:6]=='$ cd /'):
        curDir = ['/']
        continue

    if(inst[0:7]=='$ cd ..'):
        curDir = curDir[0:len(curDir)-1]
        continue

    if(inst[0:4]=='$ cd'):
        curDir.append(inst[5:len(inst)])
        continue

    if(inst[0:4]=='$ ls'):
        lsInst = 1
        while( idx + lsInst < instructions.__len__() and instructions[idx + lsInst][0]!='$'):
            thisInst = instructions[idx + lsInst]
            lsInst += 1
            if(thisInst[0:3]=='dir'):
                continue
            
            
            addFile(curDir, thisInst.split(' ')[1], int(thisInst.split(' ')[0]))

printDirStruct(dirStruct, '')

matchingDirs = []


def sumFilesInFolder(folder) -> int:
    myTotal = 0
    subfolderTotal = 0
    for fld in folder.folders:
        subfolderTotal += sumFilesInFolder(fld)
    for fi in folder.files:
        myTotal += fi.size
    folder.size = myTotal + subfolderTotal
    print(folder.name + ' : ' + str(folder.size))
    matchingDirs.append(folder.size)
    return folder.size

grandTotal = sumFilesInFolder(dirStruct)
free = 70000000 - grandTotal
needed = 30000000 - free

print(grandTotal)
print(free)
print(needed)

matchingDirs.sort()

print(matchingDirs)


for md in matchingDirs:
    if(md > needed):
        print(md)
        break
    