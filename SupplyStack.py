def crateMover9000(file):
    stackedCrates = []
    stacks_input, moves_input = file.split('\n\n')
    
    for line in stacks_input.splitlines():
        for i, index in enumerate(range(1, len(line), 4)):
            while i >= len(stackedCrates):
                stackedCrates.append([])
            if line[index] != ' ':
                stackedCrates[i].insert(0, line[index])

    nab_list = list(map(lambda x: [x[1],x[3],x[5]], map(lambda x: x.split(), moves_input.split('\n'))))
    for nab in nab_list:
        n = 0
        while n < int(nab[0]):
            stackedCrates[int(nab[2])-1].append(stackedCrates[int(nab[1])-1].pop())
            n +=1
    return ''.join(map(lambda x: x.pop(), stackedCrates))

def crateMover9001(file):
    stackedCrates = []
    stacks_input, moves_input = file.split('\n\n')

    for line in stacks_input.splitlines():
        for i, index in enumerate(range(1, len(line), 4)):
            while i >= len(stackedCrates):
                stackedCrates.append([])
            if line[index] != ' ':
                stackedCrates[i].insert(0, line[index])
    
    nab_list = list(map(lambda x: [x[1],x[3],x[5]], map(lambda x: x.split(), moves_input.split('\n'))))
    for nab in nab_list:
        stackedCrates[int(nab[2])-1].extend(stackedCrates[int(nab[1])-1][-int(nab[0]):])
        stackedCrates[int(nab[1])-1] = stackedCrates[int(nab[1])-1][0:-int(nab[0])]
    return ''.join(map(lambda x: x.pop(), stackedCrates))