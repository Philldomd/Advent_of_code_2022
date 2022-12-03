import os
import utils

import CaloriesCounter
import RockPaperScissor
import RucksackControl


print("....................................")
print("........Advent of Code 2022.........")
print("....................................")



DAY = 0
CLEAN_SLATE = 'YES'
RESOURCES = []
PAINTING = []

def clean():
    index = len(RESOURCES)-1
    if os.path.exists(RESOURCES[index]+".out"):
        os.remove(RESOURCES[index]+".out")

if DAY == 0 or DAY == 1:
    print("\n\n\no-,/O\\.-o-| Day 1 |-o-./O\\,-o\n")
    RESOURCES.append("Resources/day1.1.input")
    clean()
    index = len(RESOURCES)-1
    with utils.fileReader(RESOURCES[index]) as file:
        file_buffer = file.read()
        file.close()
        print("The elf carrying the most calories: ",CaloriesCounter.caloriesCounter(file_buffer))
        print("The top three elfes calories total: ",CaloriesCounter.caloriesCounterTopThree(file_buffer))
    PAINTING.append("\x1b[0;34;40m  ~    ~  ~      ~     ~ ~   ~     ~  ~  ~   ~   ")
    
if DAY == 0 or DAY == 2:
    print("\n\n\no-,/O\\.-o-| Day 2 |-o-./O\\,-o\n")
    RESOURCES.append("Resources/day2.1.input")
    clean()
    index = len(RESOURCES)-1
    with utils.fileReader(RESOURCES[index]) as file:
        file_buffer = file.read()
        file.close()
        print("The tournament score, as we interpreted the cheat: ", RockPaperScissor.tournament(file_buffer))
        print("The tournament score, corrected cheat: ", RockPaperScissor.tournament_cheat(file_buffer))
    PAINTING.append("\x1b[0;33;40m-~------'\x1b[0;34;40m    ~    ~ \x1b[0;33;40m'--~-----~-~----___________--")

if DAY == 0 or DAY == 3:
    print("\n\n\no-,/O\\.-o-| Day 3 |-o-./O\\,-o\n")
    RESOURCES.append("Resources/day3.1.input")
    clean()
    index = len(RESOURCES)-1
    with utils.fileReader(RESOURCES[index]) as file:
        file_buffer = file.read()
        file.close()
        print('The total priority of rucksack doubles is: ',RucksackControl.rucksackController(file_buffer))
        print('The total priority of badges is: ', RucksackControl.badgeController(file_buffer))
    PAINTING.append("\x1b[2;37;40m@@##@##\x1b[2;32;40m@\x1b[1;32;40m#\x1b[0;33;40m_/\x1b[0;34;40m ~   ~  \x1b[0;33;40m\ ' '. '.'.\x1b[0;32;40m#\x1b[2;32;40m@\x1b[2;37;40m@##|@@@#@#@@##@@@")


if DAY == 0 or DAY == 4:
    print("\n\n\n\n\--------------------\\\n >   To Be Continued  >\n/--------------------/\n\n\n")

if CLEAN_SLATE == 'YES':
    for x in RESOURCES:
        if os.path.exists(x+".out"):
            os.remove(x+".out")
if os.name == 'posix':
    print('     ________                           ________')
    print('    / +  \\   \\                         / +  \\   \\')
    print('   /______\\___\\                       /______\\___\\')
    print('_____|"""""|_____     Painting     _____|"""""|_____\n\n\n')
    while len(PAINTING) != 0:
        print(PAINTING.pop())
else:
    print("\n\nPainting is unsupported on this os: ",os.name)