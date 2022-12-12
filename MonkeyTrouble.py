from collections import deque

items = []
operations = []
tests = []
outcome = []
looked_at = []

def MonkeyInTheMiddle():
    for x, _ in enumerate(items):
        while len(items[x]) != 0:
            old = items[x].popleft()
            new = eval(operations[x])
            new = new // 3
            if new % tests[x] == 0:
                items[outcome[x][0]].append(new)
            else:
                items[outcome[x][1]].append(new)
            looked_at[x] += 1


def ThrowingItems(file_buffer):
    fi = iter(file_buffer.splitlines())
    for line in fi:
        if 'Monkey' in line:
            looked_at.append(0)
            continue
        elif 'Starting' in line:
            x = line.split(':')[1].split(',')
            items.append(deque([int(val) for val in x]))
        elif 'Operation:' in line:
            x = line.split('=')[1]
            operations.append(x)
        elif 'Test:' in line:
            x = line.split('by')[1]
            tests.append(int(x))
        elif 'If' in line:
            line1 = next(fi)
            x = line.split('monkey')[1]
            y = line1.split('monkey')[1]
            outcome.append([int(x), int(y)])
    for _ in range(20):
        MonkeyInTheMiddle()
    looked_at.sort()
    looked_at.reverse()
    print(looked_at[0]*looked_at[1])