# After reading up on enumeration in pyhton i found a new more clean solution
from collections import deque

def fineTuneDataMarker(file_buffer, markerLength):
    for index, value in enumerate(file_buffer):
        if len(set(file_buffer[index-markerLength:index])) == markerLength:
            return index

def generateTree(file_buffer, d_name):
    d_size = 0
    dir_list=[]
    file_list=[]
    line = file_buffer.popleft().split()
    if set(["$", "cd"]).issubset(set(line)):
        if line[2] != "..":
            dir_list.append(generateTree(file_buffer))
    elif set(["$", "ls"]).issubset(set(line)):
        num_pop = 0
        for new_line in file_buffer:
            li = new_line.split()
            if len(li) > 2:
                break
            else:
                file_list.append(li[0:2])
                num_pop += 1
        while num_pop != 0:
            file_buffer.popleft()
            num_pop-=1
    while len(file_buffer) > 0:
            if file_buffer[0].split()[2] != '..':
                nextDir = file_buffer[0].split()[2]
                file_buffer.popleft()
                dir_list.append(generateTree(file_buffer, nextDir))
            else:
                file_buffer.popleft()
                break
    for s, _ in file_list:
        if s.isdigit():
            d_size += int(s)
    for s in dir_list:
        d_size += int(s.get("size"))

    return dict(name = d_name, dir = dir_list, file = file_list, size = d_size)

def calcDirSize(fileSystem, range):
    value = 0
    dirs = fileSystem.get("dir")
    for dir in dirs:
        if dir.get("size") <= range:
            value += int(dir.get("size"))
        if len(dir.get("dir")) > 0:
            value += calcDirSize(dir, range)
    return int(value)

def generate(file_buffer):
    buffer = deque(file_buffer)
    line = buffer.popleft().split()
    return generateTree(buffer, line[2])

def listDirs(fileSystem):
    value = []
    dirs = fileSystem.get("dir")
    for dir in dirs:
        value.append(int(dir.get("size")))
        if len(dir.get("dir")) > 0:
            value.extend(listDirs(dir))
    return value

def filesystemCleanup(fileSystem, max, free):
    value = []
    used = fileSystem.get("size")
    range = max - free
    value.extend(listDirs(fileSystem))
    return min([item for item in value if used - item <= range])

def CycleSignalStrength(file_buffer):
    cycle_stop = 20
    cycle = 0
    signal = 1
    signals = []
    def tick():
        nonlocal signal, signals, cycle, cycle_stop
        cycle += 1
        if cycle == cycle_stop:
            signals.append(signal*cycle)
            cycle_stop += 40



    for instruction in file_buffer.splitlines():
        for command in instruction.split():
            if command == 'noop':
                tick()
            elif command == 'addx':
                tick()
                tick()
            else:    
                signal += int(command)
            
        if cycle_stop > 220:
            break
    return sum(signals)

def DrawSignal(file_buffer):
    cycle = 0
    signal = 1
    def tick():
        nonlocal cycle, signal
        if cycle % 40 in (signal-1, signal, signal+1):
            print('#', end="")
        else:
            print('.', end="")
        cycle += 1
        if cycle % 40 == 0:
            print()
        

    for instruction in file_buffer.splitlines():
        for command in instruction.split():
            if command == 'noop':
                tick()
            elif command == 'addx':
                tick()
                tick()
            else:    
                signal += int(command)
            

    