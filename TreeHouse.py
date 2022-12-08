def findNumVisibleTrees(file_buffer):
    grid = file_buffer.splitlines()
    ans = 0
    for x, row in enumerate(grid):
        for y, tree in enumerate(row):
            if all(grid[x][j] < tree for j in range(0,y)): # ->
                ans += 1
            elif all(grid[x][j] < tree for j in range(y+1,len(row))): # <-
                ans += 1
            elif all(grid[i][y] < tree for i in range(0,x)): # \/
                ans += 1
            elif all(grid[i][y] < tree for i in range(x+1,len(grid))): # /\
                ans += 1
    return ans

def findBestScenicTree(file_buffer):
    grid = file_buffer.splitlines()
    scenicValues = []
    for x, row in enumerate(grid):
        for y, tree in enumerate(row):
            up, down, left, right = [0, 0, 0, 0]
            for t in range(x-1,-1,-1):
                up += 1
                if grid[t][y] >= tree:
                    break
            if up == 0:
                continue
            for t in range(x+1, len(grid)):
                down += 1
                if grid[t][y] >= tree:
                    break
            if down == 0:
                continue
            for u in range(y-1,-1,-1):
                left += 1
                if grid[x][u] >= tree:
                    break
            if left == 0:
                continue
            for u in range(y+1,len(row)):
                right += 1
                if grid[x][u] >= tree:
                    break
            if right == 0:
                continue
            scenicValues.append(up*down*left*right)
    return max(scenicValues)
