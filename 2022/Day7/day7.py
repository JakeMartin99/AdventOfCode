class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = {}
        self.dirs = {}
        self.size = 0
    def apply_sizing(self):
        fsize = sum([f.size for f in self.files.values()])
        dsize = sum([d.apply_sizing() for d in self.dirs.values()])
        self.size = fsize + dsize
        return self.size
    def prnt(self, idt):
        print(" |--"*idt + f"Dir {self.name}: {self.size}")
        for f in self.files.values():
            f.prnt(idt+1)
        for d in self.dirs.values():
            d.prnt(idt+1)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def prnt(self, idt):
        print(" |--"*idt + f"File {self.name}: {self.size}")
    
file = open("day7.txt")
lines = file.read().split('\n')[1:]
file.close()
root = Directory("/", None)
curr = root
for l in lines:
    items = l.split(' ')
    if items[0] == '$':
        if items[1] == "cd":
            name = items[2]
            if name == "..":
                curr = curr.parent
            elif name == "/":
                curr = root
            else:
                if name not in curr.dirs.keys():
                    d = Directory(name, curr)
                    curr.dirs[name] = d
                curr = curr.dirs[name]
        elif items[1] == "ls":
            pass
    else:
        val, name = items
        if val == "dir":
            if name not in curr.dirs.keys():
                d = Directory(name, curr)
                curr.dirs[name] = d
        else:
            curr.files[name] = File(name, int(val))
root.apply_sizing()
root.prnt(0)
dirs = []
def breadth(dir):
    dirs.append(dir)
    sum = dir.size if dir.size <= 100000 else 0
    for d in dir.dirs.values():
        sum += breadth(d)
    return sum
print(breadth(root))

total_space = 70000000
req_unused = 30000000
allowed_fill = total_space - req_unused
curr_fill = root.size
req_remove = curr_fill - allowed_fill
dirs.sort(key=lambda d: d.size)
for d in dirs:
    if d.size >= req_remove:
        print(d.size)
        break