import sys

class Directory:
    def __init__(self, name):
        self.name = name
        self.type = 'd'
        self.children = {}
        self.parent = None
        self.cachedSize = None

    def addChild(self, child):
        self.children[child.name] = child
        if child.type == 'd':
            child.parent = self

    def totalSize(self):
        if self.cachedSize is None:
            self.cachedSize = sum([node.totalSize() for node in self.children.values()])
        return self.cachedSize

class FileNode:
    def __init__(self, name, fSize):
        self.name = name
        self.type = 'f'
        self.fSize = fSize

    def totalSize(self):
        return self.fSize

root = Directory('/')
allDirs = [root]

with open('07/input.txt', 'r') as f:
    pwd = root
    
    for line in f:
        # Parsing is slightly sloppy but works on well formed output.
        if line[0] == '$':
            if line == '$ cd ..\n':
                pwd = pwd.parent
            elif line == '$ cd /\n':
                pwd = root
            elif line.startswith('$ cd '):
                dirname = line.strip()[5:]
                pwd = pwd.children[dirname]
            # elif line == '$ ls\n': # do nothing.
        else:
            if line.startswith('dir '):
                dirname = line.strip()[4:]
                dirNode = Directory(dirname)
                pwd.addChild(dirNode)
                allDirs.append(dirNode)
            else:
                [size, fname] = line.strip().split(' ')
                pwd.addChild(FileNode(fname, int(size)))

smallDirs = [d for d in allDirs if d.totalSize() <= 100000]
smallDirSum = sum([d.totalSize() for d in smallDirs])
print(smallDirSum)