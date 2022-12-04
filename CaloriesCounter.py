import utils

def caloriesCounter(file):
    print("****** Calories Counter ******")
    return max(list(map(sum, list(map(lambda x: list(map(int,x)), list(map(lambda x: x.splitlines(), file.split("\n\n"))))))))

def caloriesCounterTopThree(file):
    t = list(map(sum, list(map(lambda x: list(map(int,x)), list(map(lambda x: x.splitlines(), file.split("\n\n")))))))
    t.sort()
    return sum(t[-3:])

