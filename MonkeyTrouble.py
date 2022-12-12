from collections import deque
from math import prod

items = []
operations = []
tests = []
outcome = []
looked_at = []

def MonkeyInTheMiddle(w, modmonkey):
    
    for x, _ in enumerate(items):
        while len(items[x]) != 0:
            old = items[x].popleft()
            new = eval(operations[x])
            new = eval(w)
            if new % tests[x] == 0:
                items[outcome[x][0]].append(new)
            else:
                items[outcome[x][1]].append(new)
            looked_at[x] += 1


def ThrowingItems(file_buffer, r, w):
    items.clear()
    operations.clear()
    tests.clear()
    outcome.clear()
    looked_at.clear()
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
    modmonkey = prod([tests[x] for x, _ in enumerate(tests)])
    for i in range(r):
        MonkeyInTheMiddle(w, modmonkey)
    looked_at.sort()
    looked_at.reverse()
    print(looked_at[0]*looked_at[1])


from collections import defaultdict
from math import prod


def parse_monkey(lines):
    return {
        "items": [int(x) for x in lines[1][18:].split(",")],
        "op": lambda old: eval(lines[2][19:]),
        "test": lambda x: x % int(lines[3][21:]) == 0,
        "testnum": int(lines[3][21:]),
        "throw": {
            True: int(lines[4][29:]),
            False: int(lines[5][30:]),
        },
    }


def p1(f):
    monkeys = [parse_monkey(m.splitlines()) for m in f.read().split("\n\n")]
    active = defaultdict(int)

    for r in range(20):
        for i, m in enumerate(monkeys):
            for item in m["items"]:
                active[i] += 1
                new = m["op"](item) // 3
                test = m["test"](new)
                throw = m["throw"][test]
                monkeys[throw]["items"].append(new)
            m["items"] = []

    a = sorted(active.values(), reverse=True)
    return a[0] * a[1]


def p2(f):
    monkeys = [parse_monkey(m.splitlines()) for m in f.read().split("\n\n")]
    active = defaultdict(int)
    mod = prod(m["testnum"] for m in monkeys)

    for r in range(10000):
        for i, m in enumerate(monkeys):
            for item in m["items"]:
                active[i] += 1
                new = m["op"](item) % mod
                test = m["test"](new)
                throw = m["throw"][test]
                monkeys[throw]["items"].append(new)
            m["items"] = []

    a = sorted(active.values(), reverse=True)
    return a[0] * a[1]