class Solution(object):
    def checkXMatrix(self, grid):
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if i==j:
                    if grid[i][j] == 0:
                        return False
                elif i+j == r - 1:
                    if grid[i][j] == 0:
                        return False
                elif grid[i][j] !=0:
                    return False
        return True

