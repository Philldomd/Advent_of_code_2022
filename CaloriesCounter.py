import utils

def caloriesCounter(input_path):
    print("****** Calories Counter ******")
    file = utils.fileReader(input_path)
    elfes = [0]
    elf_number = 0
    for line in file:
        if line == '\n':
            elf_number += 1
            elfes.append(0)
        else:
            elfes[elf_number] += int(line)
    file.close()
    file = utils.fileWriter(input_path+".out")
    for x in elfes:
        file.write(str(x)+'\n')
    file.close
    elfes.sort()
    return elfes,elf_number

