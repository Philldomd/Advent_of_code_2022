import utils

def winner(t_elf, t_me):
    win = 0 if t_elf > t_me else 6 if t_me > t_elf else 3
    point = 6 if t_me + t_elf == 4 and win == 0 else 0 if t_me + t_elf == 4 and win == 6 else win
    point += t_me
    return point

def calcStrategy(t_elf,outcome):
    elf = t_elf-1
    strat = (elf + 1) % 3 if outcome == 'Z' else (elf - 1) % 3 if outcome == 'X' else elf
    return strat + 1

def tournament(file):
    print("****** Tournament ******")
    score = 0
    for line in file.splitlines():
        elf, me = str(line).split(" ")
        t_elf = 1 if elf == 'A' else 2 if elf == 'B' else 3 if elf == 'C' else 0
        t_me = 1 if me == 'X' else 2 if me == 'Y' else 3 if me == 'Z' else 0
        score += winner(t_elf, t_me)
    return score

def tournament_cheat(file):
    score = 0
    for line in file.splitlines():
        elf, outcome = str(line).split(" ")
        t_elf = 1 if elf == 'A' else 2 if elf == 'B' else 3 if elf == 'C' else 0
        t_me = calcStrategy(t_elf, outcome)
        score += winner(t_elf, t_me)
    return score