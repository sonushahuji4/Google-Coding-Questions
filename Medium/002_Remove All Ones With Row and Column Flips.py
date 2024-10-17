# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/description/

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        row, col = len(grid), len(grid[0])
        
        for i in range(row):
            if grid[i][0] == 1:
                for j in range(col):
                    grid[i][j] ^= 1
		
        for j in range(1, col):
            if sum([grid[i][j] for i in range(row)]) not in [0, row]:
                return False
        
        return True
