import utils

def priorityCalc(char):
    dec_char = ord(char)
    return dec_char - 96 if dec_char >= 97 else dec_char - 38

def rucksackController(file):
    print("****** Rucksack control ******")
    priority_sum = 0

    for line in file.split('\n'):
        firstComp, secondComp = line[:len(line)//2],line[len(line)//2:]
        comp = set(firstComp) & set(secondComp)
        priority_sum += priorityCalc(comp.pop())

    return priority_sum

def badgeController(file):
    priority_sum = 0
    fi = iter(file.split('\n'))
    for line1 in fi:
        line2 = next(fi)
        line3 = next(fi)
        badge = set(line1) & set(line2) & set(line3)
        priority_sum += priorityCalc(badge.pop())

    return priority_sum

def compareCompartments(firstComp, secondComp, char_index):
    priority = 0
    if char_index == len(firstComp):
        return priority
    else:
        size = len(secondComp)
        temp = secondComp.replace(firstComp[char_index], '')
        if size > len(temp):
            priority = priorityCalc(firstComp[char_index])
        char_index += 1
        priority += compareCompartments(firstComp, temp, char_index)
        return priority

def rucksackControllerOld(input_path):
    print("****** Rucksack control ******")
    priority_sum = 0
    for line in input_path.split('\n'):
        line = line.rstrip()
        firstComp, secondComp = line[:len(line)//2],line[len(line)//2:]
        priority_sum += compareCompartments(firstComp, secondComp, 0)

    return priority_sum

def findBadge(first, second, third, char_index):
    priority = 0
    if char_index == len(first):
        return priority
    else:
        size2 = len(second)
        size3 = len(third)
        temp2 = second.replace(first[char_index], '')
        temp3 = third.replace(first[char_index], '')
        if size2 > len(temp2) and size3 > len(temp3):
            return priorityCalc(first[char_index])
        char_index +=1
        return findBadge(first, temp2, temp3, char_index)

def badgeControllerOld(input_path):
    priority_sum = 0
    fi = iter(input_path.split('\n'))
    for line1 in fi:
        line2 = next(fi)
        line3 = next(fi)
        priority_sum += findBadge(line1.rstrip(), line2.rstrip(), line3.rstrip(), 0)

    return priority_sum

            