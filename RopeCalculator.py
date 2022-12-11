def CalculateTailsPositions(file_buffer):
    head = [0,0]
    head_prev = [0,0]
    tail = [0,0]
    all_tails = ['0,0']

    for row in file_buffer.splitlines():
        dir, x = row.split()
        itr = int(x)
        while itr != 0:
            head_prev=head.copy()
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
            if head[0] not in set([tail[0]-1, tail[0], tail[0]+1]):
                tail=head_prev
                all_tails.append(str(tail))
            elif head[1] not in set([tail[1]-1, tail[1], tail[1]+1]):
                tail=head_prev.copy()
                all_tails.append(str(tail))
    trail = list(dict.fromkeys(all_tails))
    return len(trail)
