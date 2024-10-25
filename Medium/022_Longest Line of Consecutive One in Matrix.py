# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/description/

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        def dfs(i, j):
            nonlocal memo
            # base case: going outside matrix boundaries and when element is 0
            if  i < 0 or j < 0 or j >= n or i >= m or mat[i][j] == 0:
                return [0, 0, 0, 0]
            
            # no need to compute again if already computed for a cell
            if memo.get((i,j)):
                return memo[(i,j)]
            
            # get the horizontal sum, +1 for current cell
            hsum = dfs(i, j+1)[0] + 1
            
            # get the vertical sum, +1 for current cell
            vsum = dfs(i+1, j)[1] + 1
            
            # get the diagonal sum, +1 for current cell
            dsum = dfs(i+1, j+1)[2] + 1
            
            # get the anti-diagonal sum, +1 for current cell
            adsum = dfs(i+1, j-1)[3] + 1
            
            # save and return the lengths of lines from a given cell in all directions
            memo[(i,j)] = [hsum, vsum, dsum, adsum]
            return memo[(i,j)]
        
        m, n = len(mat), len(mat[0])
        result = 0
        memo = {}
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    # dfs() returns the lengths of lines from the cell mat[row, col] in all directions.
                    # Get the longest line and compare it with longest lines from other cells
                    result = max(max(dfs(row, col)), result)
        return result
