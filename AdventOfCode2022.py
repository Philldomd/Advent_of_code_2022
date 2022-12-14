import os
import utils

import CaloriesCounter
import RockPaperScissor
import RucksackControl
import CampCleanup
import SupplyStack
import CommunicationTuning
import TreeHouse
import RopeCalculator
import MonkeyTrouble


print("....................................")
print("........Advent of Code 2022.........")
print("....................................")



DAY = 13

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
    print("\n\n\no-,/O\\.-o-| Day 6 |-o-./O\\,-o\n")
    with utils.fileReader("Resources/day6.input") as file:
        file_buffer = file.read()
        file.close()
        DATA_MARKER_LENGTH = 4
        MESSAGE_MARKER_LENGTH = 14
        if os.name == 'posix':
            print('The first unique sequence of four letters, the data starts after: \x1b[0;33;40m', CommunicationTuning.fineTuneDataMarker(file_buffer, DATA_MARKER_LENGTH),'\x1b[0;37;40m')
            print('The Elves has the following number of shared cleaning areas: \x1b[0;33;40m', CommunicationTuning.fineTuneDataMarker(file_buffer, MESSAGE_MARKER_LENGTH),'\x1b[0;37;40m')
        else:
            print('The first unique sequence of four letters, the data marker starts at: ', CommunicationTuning.fineTuneDataMarker(file_buffer, DATA_MARKER_LENGTH))
            print('The first unique sequence of fourteen letters, the data message starts at: ', CommunicationTuning.fineTuneDataMarker(file_buffer, MESSAGE_MARKER_LENGTH))

if DAY == 0 or DAY == 7:
    print("\n\n\no-,/O\\.-o-| Day 7 |-o-./O\\,-o\n")
    with utils.fileReader("Resources/day7.input") as file:
        file_buffer = file.read()
        file.close()
        DISK_MAX = 70000000
        FREE_SPACE = 30000000
        Tree = CommunicationTuning.generate(file_buffer.splitlines())
        if os.name == 'posix':
            print('The total of all folders under 100000 in size: \x1b[0;33;40m', CommunicationTuning.calcDirSize(Tree, 100000),'\x1b[0;37;40m')
            print('The most suitable folder to remove: \x1b[0;33;40m', CommunicationTuning.filesystemCleanup(Tree, DISK_MAX, FREE_SPACE),'\x1b[0;37;40m')
        else:
            print('The total of all folders under 100000 in size: ', CommunicationTuning.calcDirSize(Tree, 100000))
            print('The most suitable folder to remove: ', CommunicationTuning.filesystemCleanup(Tree, DISK_MAX, FREE_SPACE))


if DAY == 0 or DAY == 8:
    print("\n\n\no-,/O\\.-o-| Day 8 |-o-./O\\,-o\n")
    with utils.fileReader("Resources/day8.input") as file:
        file_buffer = file.read()
        file.close()
        if os.name == 'posix':
            print('Number of visible trees in this forest: \x1b[0;33;40m', TreeHouse.findNumVisibleTrees(file_buffer),'\x1b[0;37;40m')
            print('Tree with the highest scenic value: \x1b[0;33;40m', TreeHouse.findBestScenicTree(file_buffer),'\x1b[0;37;40m')
        else:
            print('Number of visible trees in this forest: ', TreeHouse.findNumVisibleTrees(file_buffer))
            print('Tree with the highest scenic value: ', TreeHouse.findBestScenicTree(file_buffer))

if DAY == 0 or DAY == 9:
    print("\n\n\no-,/O\\.-o-| Day 9 |-o-./O\\,-o\n")
    with utils.fileReader("Resources/day9.input") as file:
        file_buffer = file.read()
        file.close()
        if os.name == 'posix':
            print('Number of visited nodes for tail, short rope: \x1b[0;33;40m', RopeCalculator.CalculateTailsPositions(file_buffer,2),'\x1b[0;37;40m')
            print('Number of visited nodes for tail, long rope: \x1b[0;33;40m', RopeCalculator.CalculateTailsPositions(file_buffer,10),'\x1b[0;37;40m')
        else:
            print('Number of visited nodes for tail, short rope: ', RopeCalculator.CalculateTailsPositions(file_buffer,2))
            print('Number of visited nodes for tail, long rope: ', RopeCalculator.CalculateTailsPositions(file_buffer,10))

if DAY == 0 or DAY == 10:
    print("\n\n\no-,/O\\.-o-| Day 10 |-o-./O\\,-o\n")
    with utils.fileReader("Resources/day10.input") as file:
        file_buffer = file.read()
        file.close()
        print('The value of x in all cycles: ', CommunicationTuning.CycleSignalStrength(file_buffer))
        print('CRT print: \n')
        CommunicationTuning.DrawSignal(file_buffer)

if DAY == 0 or DAY == 11:
    print("\n\n\no-,/O\\.-o-| Day 11 |-o-./O\\,-o\n")
    with utils.fileReader("Resources/day11.input") as file:
        file_buffer = file.read()
        file.close()
        MonkeyTrouble.ThrowingItems(file_buffer, 20, 'new // 3')
        MonkeyTrouble.ThrowingItems(file_buffer, 10000, 'new % modmonkey')

if DAY == 0 or DAY == 12:
    print("\n\n\no-,/O\\.-o-| Day 12 |-o-./O\\,-o\n")
    with utils.fileReader("Resources/day12.input") as file:
        file_buffer = file.read()
        file.close()
        CommunicationTuning.FindBestSignalSpot(file_buffer)
        CommunicationTuning.FindBestHickingTrail(file_buffer)

if DAY == 0 or DAY == 13:
    print("\n\n\no-,/O\\.-o-| Day 13 |-o-./O\\,-o\n")
    with utils.fileReader("Resources/day13.input") as file:
        file_buffer = file.read()
        file.close()
        CommunicationTuning.DistresSignal(file_buffer)
        CommunicationTuning.SortOutSignal(file_buffer)

if DAY == 0 or DAY == 14:
    print("\n\n\n\n\--------------------\\\n >   To Be Continued  >\n/--------------------/\n\n\n")

if os.name == 'posix' and DAY == 1000:
    print('      \x1b[4;37;40m        \x1b[0;37;40m                              \x1b[4;37;40m        \x1b[0;37;40m')
    print('     / \x1b[4;33;40m++\x1b[0;37;40m \\   \\                            / \x1b[4;33;40m++\x1b[0;37;40m \\   \\')
    print('    \x1b[4;37;40m/      \\   \\\x1b[0;37;40m                          \x1b[4;37;40m/      \\   \\\x1b[0;37;40m')
    print('\x1b[4;37;40m  \x1b[4;35;40m%\x1b[4;37;40m  \x1b[0;37;40m|\x1b[4;31;40m"m"m"\x1b[0;37;40m|\x1b[4;37;40m   |  \x1b[4;34;40m~\x1b[0;37;40m_     \x1b[1;33;40mPainting\x1b[0;37;40m     ___\x1b[4;33;40m~\x1b[0;37;40m_|\x1b[4;31;40m"m"u"\x1b[0;37;40m|\x1b[4;37;40m   |\x1b[4;32;40m¤\x1b[4;37;40m \x1b[0;37;40m\n\n\n')
    while len(PAINTING) != 0:
        print(PAINTING.pop())
elif os.name != 'posix' and DAY == 1000:
    print("\n\nPainting is unsupported on this os: ",os.name)