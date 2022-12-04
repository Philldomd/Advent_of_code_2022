# I wanted to try and solve this using maps and lambda functions as far as i could. I know that it might be really hard to follow but i tried to make it more clear.

irange = lambda x,y: range(x, y + 1) # Borrowed this from oliver-ni for a cleaner range set
isSubSet = lambda x,y: set(x).issubset(set(y)) or set(y).issubset(set(x)) # Inspired by the entry above to solve issubset
isDisjoint = lambda x,y: set(x).isdisjoint(set(y)) # Inspired by oliver-ni above to solve isdisjoint

def cleanupOverlap(file):
    return sum(                                                                                                                                 # Sum up all entries of 1 and 0
        list(map(lambda change: 1 if change else 0,                                                                                             # Return 1 for true and 0 for false
                 list(map(lambda set_element: isSubSet(set_element[0], set_element[1]),                                                         # Checks if range set A contains B or B contains A
                          list(map(lambda element:                                                                                              # x, contains list of ranges [[2,3,4],[3,4,5]]
                                   list(map(lambda c:                                                                                           # c, contains each entry as string, '2-5'
                                            list(irange(*map(int,c.split('-')))), element)),list(map(lambda line: line.split(','), file.split('\n')))))))))) # Read file and split on '\n' and ',', then create a list of ranges instead

def cleanupOverlapFineGranular(file):
    return sum(                                                                                                                                  # Sum up all entries of 1 and 0
        list(map(lambda change: 0 if change else 1,                                                                                              # Return 0 if they are disjointed and 1 otherwise
                 list(map(lambda set_element: isDisjoint(set_element[0], set_element[1]),                                                        # Checks if range set A share any elements with B
                          list(map(lambda element:                                                                                               # x, contains list of ranges [[2,3,4],[3,4,5]]
                                   list(map(lambda c:                                                                                            # c, contains each entry as string, '2-5'
                                            list(irange(*map(int, c.split('-')))), element)),list(map(lambda line: line.split(','), file.split('\n')))))))))) # Read file and split on '\n' and ',', then create a list of ranges instead
