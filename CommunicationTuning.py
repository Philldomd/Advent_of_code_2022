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
            
def FindBestSignalSpot(file_buffer):
    def adj(i, j):
        return (i, j-1), (i+1, j), (i, j+1), (i-1, j)
    

    grid = {
        (i,j): x
        for i, row in enumerate(file_buffer.splitlines())
        for j, x in enumerate(row)
    }
    start = next(k for k, v in grid.items() if v == 'S')
    end = next(k for k, v in grid.items() if v == 'E')
    grid[start] = 'a'
    grid[end] = 'z'

    visited = {}
    queue = deque([(0,start)])

    while len(queue) > 0:
        t, p = queue.popleft()
        if p in visited:
            continue
        visited[p]=t
        val = ord(grid[p])
        for n in adj(*p):
            n_val = ord(grid.get(n, '{'))
            if n_val - val > 1:
                continue
            queue.append((t+1, n))

    print(visited[end])

def FindBestHickingTrail(file_buffer):
    def adj(i, j):
        return (i, j-1), (i+1, j), (i, j+1), (i-1, j)
    

    grid = {
        (i,j): x
        for i, row in enumerate(file_buffer.splitlines())
        for j, x in enumerate(row)
    }
    start = next(k for k, v in grid.items() if v == 'S')
    end = next(k for k, v in grid.items() if v == 'E')
    grid[start] = 'a'
    grid[end] = 'z'
    startpositions = []

    for k, v in grid.items():
        if v == 'a':
            startpositions.append(k)
    lengths = []

    for starts in startpositions:
        visited = {}
        queue = deque([(0,starts)])
        while len(queue) > 0:
            t, p = queue.popleft()
            if p in visited:
                continue
            visited[p]=t
            val = ord(grid[p])
            for n in adj(*p):
                n_val = ord(grid.get(n, '{'))
                if n_val - val > 1:
                    continue
                queue.append((t+1, n))
        if end in visited:
            lengths.append(visited[end])

    
    print(min(lengths))

def cmp(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x - y

    if isinstance(x, list) and isinstance(y, list):
        for i, j in zip(x, y):
            result = cmp(i,j)
            if result != 0:
                return result
        return len(x) - len(y)
    
    if isinstance(x, list):
        return cmp(x, [y])

    if isinstance(y, list):
        return cmp([x], y)

    assert False

def DistresSignal(file_buffer):
    signals = [[eval(x), eval(y)] for x, y in list(map(lambda x: x.split() , file_buffer.split('\n\n')))]
    values = 0
    for i, signal in enumerate(signals):
        if cmp(*signal) < 0:
            values += i + 1
        
    print(values)

def SortOutSignal(file_buffer):
    signals = [[eval(x)] for x in file_buffer.split() if len(x) > 0]
    signals.append(eval('[[6]]'))
    signals.append(eval('[[2]]'))
    n = len(signals)
    for i in range(n):
        done = True
        for j in range(n - i - 1):
            if cmp(signals[j], signals[j + 1]) > 0:
                signals[j], signals[j + 1] = signals[j + 1], signals[j]
                done = False
        if done:
            break

    print((signals.index([[6]])+1) * (signals.index([[2]])+1))                

