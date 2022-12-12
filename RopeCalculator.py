def move(head, tail):
    pdiff = [head[0]-tail[0], head[1]-tail[1]]
    diff = [min(1, max(-1, x)) for x in pdiff]
    if diff == pdiff:
        return tail
    return [tail[0]+diff[0], tail[1]+diff[1]]

def CalculateTailsPositions(file_buffer, length):
    rope = []
    l = length
    while l != 0:
        rope.append([0,0])
        l -= 1 
    head = rope[0]
    all_tails = ['[0, 0]']

    for row in file_buffer.splitlines():
        dir, x = row.split()
        itr = int(x)
        while itr != 0:
            itr -= 1
            # Move head,
            if 'U' == dir:
                head[0] += 1
            elif 'D' == dir:
                head[0] -= 1
            elif 'R' == dir:
                head[1] += 1
            elif 'L' == dir:
                head[1] -= 1
            # Check tail
            i = 1
            while i != length:
                rope[i]=move(rope[i-1], rope[i])
                if (i == length-1):
                    all_tails.append(str(rope[i]))
                i += 1
    trail = list(dict.fromkeys(all_tails))
    return len(trail)
