# https://leetcode.com/problems/battleships-in-a-board/description/

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        # Approach One DFS
        def getNumberOfBattleShips(eachRow, eachCol, row, col):
            board[eachRow][eachCol] = "."
            directionToMoveIn = [(-1,0),(1,0),(0,-1),(0,1)]
            
            for x, y in directionToMoveIn:
                dx = x + eachRow
                dy = y + eachCol
                if dx in range(row) and dy in range(col) and board[dx][dy] == 'X':
                    getNumberOfBattleShips(dx, dy, row, col)

        row = len(board)
        col = len(board[0])
        numberOfBattleships = 0
        for eachRow in range(row):
            for eachCol in range(col):
                if board[eachRow][eachCol] == 'X':
                    numberOfBattleships += 1
                    getNumberOfBattleShips(eachRow, eachCol, row, col)
        return numberOfBattleships
    
