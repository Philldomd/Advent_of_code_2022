def ThrowingItems(file_buffer):
    items = []
    operations = []
    tests = []
    outcome = []
    fi = iter(file_buffer.splitlines())
    for line in fi:
        if 'Monkey' in line:
            continue
        elif 'Starting' in line:
            x = line.split(':')[1].split(',')
            items.append([int(val) for val in x])
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