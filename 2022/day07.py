#!/usr/bin/env python3

class dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = {}
        self.dirs = {}
    
    def add_dir(self, dir_name):
        self.dirs[dir_name] = dir(dir_name, self)
        
    def add_file(self, filename, size):
        self.files[filename] = size
    
    def get_dir(self, dir_name):
        return self.dirs[dir_name]
    
    def get_size(self):
        ans = sum(self.files.values())
        for directory in self.get_dirs():
            ans += directory.get_size()
        return ans
    
    def get_dirs(self):
        for k in self.dirs.keys():
            yield self.dirs[k]

def list_small_dirs(filesystem):
    ans = 0
    
    if filesystem.get_size() <= 100000:
        ans = filesystem.get_size()
    
    for directory in filesystem.get_dirs():
        ans += list_small_dirs(directory)
        
    return ans
    
def parse_filesystem(data):
    filesystem = dir("/", None)
    location = filesystem
    parse_ls = False
    
    for line in data:
        line = line.strip()
        
        if parse_ls:
            if line[0] == "$":
                parse_ls = False
            elif line[0:3] == "dir":
                location.add_dir(line[4:])
                continue
            else:
                tmp = line.split(" ")
                location.add_file(tmp[1], int(tmp[0]))
                continue
        
        if line == "$ cd /":
            location = filesystem
            
        elif line[0:4] == "$ cd":
            tmp = line[5:]
            if tmp == "..":
                location = location.parent
            else:
                location = location.get_dir(tmp)
        
        elif line == "$ ls":
            parse_ls = True
            
        else:
            print(f"unknown command '{line}'")
            exit(1)
            
    return filesystem

def solution1(fs):
    return list_small_dirs(fs)

def find_dir_sizes(fs):
    yield fs.get_size()
    for directory in fs.get_dirs():
        yield from find_dir_sizes(directory)

def solution2(fs):
    
    free_space = 70000000 - fs.get_size()
    space_needed = 30000000 - free_space
    
    min_dir_size = 70000000
    
    for dir_size in find_dir_sizes(fs):
        if space_needed <= dir_size < min_dir_size:
            min_dir_size = dir_size
            
    return min_dir_size

if __name__ == "__main__":
    with open("day7.txt") as f:
        fs = parse_filesystem(f)
        print(solution1(fs))
        print(solution2(fs))

