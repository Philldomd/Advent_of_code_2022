import os
import utils

import CaloriesCounter
import RockPaperScissor
import RucksackControl
import CampCleanup
import SupplyStack


print("....................................")
print("........Advent of Code 2022.........")
print("....................................")



DAY = 0

PAINTING = []

if DAY == 0 or DAY == 1:
    print("\n\n\no-,/O\\.-o-| Day 1 |-o-./O\\,-o\n")
    with utils.fileReader("Resources/day1.input") as file:
        file_buffer = file.read()
        file.close()
        if os.name == 'posix':
            print("The elf carrying the most calories: \x1b[0;33;40m",CaloriesCounter.caloriesCounter(file_buffer), '\x1b[0;37;40m')
            print("The top three elfes calories total: \x1b[0;33;40m",CaloriesCounter.caloriesCounterTopThree(file_buffer), '\x1b[0;37;40m')
        else:
            print("The elf carrying the most calories: ",CaloriesCounter.caloriesCounter(file_buffer))
            print("The top three elfes calories total: ",CaloriesCounter.caloriesCounterTopThree(file_buffer))
    PAINTING.append("\x1b[0;34;40m  ~    ~  ~      ~     ~ ~   ~     ~  ~  ~   ~   \x1b[0;37;40m")
    
if DAY == 0 or DAY == 2:
    print("\n\n\no-,/O\\.-o-| Day 2 |-o-./O\\,-o\n")
    with utils.fileReader("Resources/day2.input") as file:
        file_buffer = file.read()
        file.close()
        if os.name == 'posix':
            print("The tournament score, as we interpreted the cheat: \x1b[0;33;40m", RockPaperScissor.tournament(file_buffer), '\x1b[0;37;40m')
            print("The tournament score, corrected cheat: \x1b[0;33;40m", RockPaperScissor.tournament_cheat(file_buffer), '\x1b[0;37;40m')
        else:
            print("The tournament score, as we interpreted the cheat: ", RockPaperScissor.tournament(file_buffer))
            print("The tournament score, corrected cheat: ", RockPaperScissor.tournament_cheat(file_buffer))
    PAINTING.append("\x1b[0;33;40m-~------'\x1b[0;34;40m    ~    ~ \x1b[0;33;40m'--~-----~-~----___________--\x1b[0;37;40m")

if DAY == 0 or DAY == 3:
    print("\n\n\no-,/O\\.-o-| Day 3 |-o-./O\\,-o\n")
    with utils.fileReader("Resources/day3.input") as file:
        file_buffer = file.read()
        file.close()
        if os.name == 'posix':
            print('The total priority of rucksack doubles is: \x1b[0;33;40m', RucksackControl.rucksackController(file_buffer), '\x1b[0;37;40m')
            print('The total priority of badges is: \x1b[0;33;40m', RucksackControl.badgeController(file_buffer), '\x1b[0;37;40m')
        else:
            print('The total priority of rucksack doubles is: ', RucksackControl.rucksackController(file_buffer))
            print('The total priority of badges is: ', RucksackControl.badgeController(file_buffer))
    PAINTING.append("\x1b[2;37;40m#@@@#\x1b[0;32;40m#\x1b[2;32;40m@\x1b[0;32;40m@@\x1b[0;33;40m_/\x1b[0;34;40m ~   ~  \x1b[0;33;40m\ ' '. '.'.\x1b[0;32;40m#\x1b[2;32;40m#\x1b[2;37;40m@@@@@#@@@@@@@@##@\x1b[0;37;40m")

if DAY == 0 or DAY == 4:
    print("\n\n\no-,/O\\.-o-| Day 4 |-o-./O\\,-o\n")
    with utils.fileReader("Resources/day4.input") as file:
        file_buffer = file.read()
        file.close()
        if os.name == 'posix':
            print('The Elves has the following number of fully contained sets: \x1b[0;33;40m', CampCleanup.cleanupOverlap(file_buffer),'\x1b[0;37;40m')
            print('The Elves has the following number of shared cleaning areas: \x1b[0;33;40m', CampCleanup.cleanupOverlapFineGranular(file_buffer),'\x1b[0;37;40m')
        else:
            print('The Elves has the following number of fully contained sets: ', CampCleanup.cleanupOverlap(file_buffer))
            print('The Elves has the following number of shared cleaning areas: ', CampCleanup.cleanupOverlapFineGranular(file_buffer))
    PAINTING.append("\x1b[2;37;40m#@##@#@@#\x1b[0;32;40m@\x1b[0;32;40m#\x1b[0;33;40m.'\x1b[0;34;40m ~  \x1b[0;33;40m'.\x1b[1;37;40m/\\\x1b[0;33;40m'.\x1b[1;37;40m/\\\x1b[0;33;40m' .\x1b[2;32;40m@\x1b[1;32;40m#\x1b[0;32;40m@\x1b[2;37;40m@@@##@@@@##@@@@@@#\x1b[0;37;40m")

if DAY == 0 or DAY == 5:
    print("\n\n\no-,/O\\.-o-| Day 5 |-o-./O\\,-o\n")
    with utils.fileReader("Resources/day5.input") as file:
        file_buffer = file.read()
        file.close()
        if os.name == 'posix':
            print('The Elves has the following number of fully contained sets: \x1b[0;33;40m', SupplyStack.crateMover9000(file_buffer),'\x1b[0;37;40m')
            print('The Elves has the following number of shared cleaning areas: \x1b[0;33;40m', SupplyStack.crateMover9001(file_buffer),'\x1b[0;37;40m')
        else:
            print('The Elves has the following number of fully contained sets: ', SupplyStack.crateMover9000(file_buffer))
            print('The Elves has the following number of shared cleaning areas: ', SupplyStack.crateMover9001(file_buffer))
    PAINTING.append("\x1b[2;37;40m#@@@@##@@#")


if DAY == 0 or DAY == 6:
    print("\n\n\n\n\--------------------\\\n >   To Be Continued  >\n/--------------------/\n\n\n")

if os.name == 'posix':
    print('      \x1b[4;37;40m        \x1b[0;37;40m                              \x1b[4;37;40m        \x1b[0;37;40m')
    print('     / \x1b[4;33;40m++\x1b[0;37;40m \\   \\                            / \x1b[4;33;40m++\x1b[0;37;40m \\   \\')
    print('    \x1b[4;37;40m/      \\   \\\x1b[0;37;40m                          \x1b[4;37;40m/      \\   \\\x1b[0;37;40m')
    print('\x1b[4;37;40m  \x1b[4;35;40m%\x1b[4;37;40m  \x1b[0;37;40m|\x1b[4;31;40m"m"m"\x1b[0;37;40m|\x1b[4;37;40m   |  \x1b[4;34;40m~\x1b[0;37;40m_     \x1b[1;33;40mPainting\x1b[0;37;40m     ___\x1b[4;33;40m~\x1b[0;37;40m_|\x1b[4;31;40m"m"u"\x1b[0;37;40m|\x1b[4;37;40m   |\x1b[4;32;40m¤\x1b[4;37;40m \x1b[0;37;40m\n\n\n')
    while len(PAINTING) != 0:
        print(PAINTING.pop())
else:
    print("\n\nPainting is unsupported on this os: ",os.name)