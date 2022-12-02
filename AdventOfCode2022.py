import os

import CaloriesCounter
import RockPaperScissor

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
    elfes, last_elf = CaloriesCounter.caloriesCounter(RESOURCES[index])
    print("The elf carrying the most calories: ",elfes[last_elf])
    print("The top three elfes calories total: ",elfes[last_elf]+elfes[last_elf-1]+elfes[last_elf-2])
    PAINTING.append("\x1b[0;34;40m  ~    ~  ~      ~     ~ ~   ~     ~  ~  ~   ~   ")
    
if DAY == 0 or DAY == 2:
    print("\n\n\no-,/O\\.-o-| Day 2 |-o-./O\\,-o\n")
    RESOURCES.append("Resources/day2.1.input")
    clean()
    index = len(RESOURCES)-1
    score = RockPaperScissor.tournament(RESOURCES[index])
    print("The tournament score, as we interpreted the cheat: ", score)
    score = RockPaperScissor.tournament_cheat(RESOURCES[index])
    print("The tournament score, corrected cheat: ", score)
    PAINTING.append("\x1b[0;33;40m-~------'\x1b[0;34;40m    ~    ~ \x1b[0;33;40m'--~-----~-~----___________--")

    

if DAY == 0 or DAY == 3:
    print("\n\n\n\n\--------------------\\\n >   To Be Continued  >\n/--------------------/\n\n\n")

if CLEAN_SLATE == 'YES':
    for x in RESOURCES:
        if os.path.exists(x+".out"):
            os.remove(x+".out")
if os.name == 'posix':
    print('_____|"""""|_____     Painting     _____|"""""|_____\n\n\n')
    while len(PAINTING) != 0:
        print(PAINTING.pop())
else:
    print("Painting is unsupported on this os: ",os.name)