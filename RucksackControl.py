def priorityCalc(char):
    dec_char = ord(char)
    return dec_char - 96 if dec_char >= 97 else dec_char - 38

def rucksackController(file):
    print("****** Rucksack control ******")
    priority_sum = 0

    for line in file.splitlines():
        firstComp, secondComp = line[:len(line)//2],line[len(line)//2:]
        comp = set(firstComp) & set(secondComp)
        priority_sum += priorityCalc(comp.pop())

    return priority_sum

def badgeController(file):
    priority_sum = 0
    fi = iter(file.splitlines())
    for line1 in fi:
        line2 = next(fi)
        line3 = next(fi)
        badge = set(line1) & set(line2) & set(line3)
        priority_sum += priorityCalc(badge.pop())

    return priority_sum