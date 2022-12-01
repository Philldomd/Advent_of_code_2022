import os

def fileReader(input_path):
    try:
        return open(input_path,'r')
    except FileNotFoundError:
        print("File not found exception: ",input_path)
    except NameError:
        print("Could not evaluate input path, not correct name: ",input_path)

def fileWriter(output_path):
    try:
        return open(output_path,'x')
    except FileNotFoundError:
        print("File not found exception: ",output_path)
    except NameError:
        print("Could not evaluate input path, not correct name: ",output_path)
    except FileExistsError:
        print("Could not create file: ",output_path," file already exists")

def caloriesCounter(input_path):
    print("\n\n************ Calories Counter ************")
    file = fileReader(input_path)
    elfes = [0]
    elf_number = 0
    for line in file:
        if line == '\n':
            elf_number += 1
            elfes.append(0)
        else:
            elfes[elf_number] += int(line)
    file.close()
    file = fileWriter(input_path+".out")
    for x in elfes:
        file.write(str(x)+'\n')
    file.close
    elfes.sort()
    return elfes,elf_number

print("....................................")
print("........Advent of Code 2022.........")
print("....................................")

DAY = 0
CLEAN_SLATE = 'YES'
RESOURCES = []

if DAY == 0 or DAY == 1:
    RESOURCES.append("Resources/day1.1.input")
    index = len(RESOURCES)-1
    if os.path.exists(RESOURCES[index]+".out"):
        os.remove(RESOURCES[index]+".out")
    elfes, last_elf = caloriesCounter(RESOURCES[index])
    print("The elf carrying the most calories: ",elfes[last_elf])
    print("The top three elfes calories total: ",elfes[last_elf]+elfes[last_elf-1]+elfes[last_elf-2])
    
if DAY == 0 or DAY == 2:
    print("\n\n\n\n\--------------------\\\n >   To Be Continued  >\n/--------------------/")

if CLEAN_SLATE == 'YES':
    for x in RESOURCES:
        if os.path.exists(x+".out"):
            os.remove(x+".out")