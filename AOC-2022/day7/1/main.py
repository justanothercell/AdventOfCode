from typing import Union

with open('input.txt') as infile:
    logs = infile.readlines()

# total that is <= 100000: 95437
# logs = [
#     '$ cd /',
#     '$ ls',
#     'dir a',
#     '14848514 b.txt',
#     '8504156 c.dat',
#     'dir d',
#     '$ cd a',
#     '$ ls',
#     'dir e',
#     '29116 f',
#     '2557 g',
#     '62596 h.lst',
#     '$ cd e',
#     '$ ls',
#     '584 i',
#     '$ cd ..',
#     '$ cd ..',
#     '$ cd d',
#     '$ ls',
#     '4060174 j',
#     '8033020 d.log',
#     '5626152 d.ext',
#     '7214296 k',
#]


class Dir:
    def __init__(self, name: str, parent: Union['Dir', None]):
        self.name = name
        self.parent = parent
        self.files: dict[str, File] = {}
        self.dirs: dict[str, Dir] = {}

    def __len__(self):
        return sum(len(d) for d in self.dirs.values()) + sum(len(f) for f in self.files.values())

    def traverse(self, state, fun):
        state = fun(state, self)
        for d in self.dirs.values():
            state = d.traverse(state, fun)
        return state


class File:
    def __init__(self, size: int):
        self.size = size

    def __len__(self):
        return self.size


class FileSystem:
    def __init__(self):
        self.root = Dir('/', None)
        self.dir = self.root

    def cd(self, directory):
        if directory == '..':
            if self.dir.parent is not None:
                self.dir = self.dir.parent
        elif directory == '/':
            self.dir = self.root
        else:
            if directory not in self.dir.dirs:
                self.dir.dirs[directory] = Dir(directory, self.dir)
            self.dir = self.dir.dirs[directory]


line = 0

fs = FileSystem()

while line < len(logs):
    if logs[line].startswith('$ cd'):
        fs.cd(logs[line][5:].strip())
    if logs[line].strip() == '$ ls':
        line += 1
        while line < len(logs) and not logs[line].startswith('$'):
            (arg, name) = logs[line].strip().split()
            if arg == 'dir':
                if name not in fs.dir.dirs:
                    fs.dir.dirs[name] = Dir(name, fs.dir)
            else:
                if name not in fs.dir.files:
                    fs.dir.files[name] = File(int(arg))
            line += 1
        line -= 1
    line += 1


def path_to_dir(d: Dir):
    if d.parent is None:
        return '~'
    return path_to_dir(d.parent) + '/' + d.name


def acc_less_100k(t: int, directory: Dir):
    print(path_to_dir(directory))
    size = len(directory)
    print(size)
    t += size if size <= 100000 else 0
    return t


total = fs.root.traverse(0, acc_less_100k)

print('total that is <= 100000:', total)  # total that is <= 100000: 1427048
