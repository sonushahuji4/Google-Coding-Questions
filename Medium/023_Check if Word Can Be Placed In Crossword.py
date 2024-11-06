# https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/description/


from typing import List

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        colsLength = len(board)
        rowsLength = len(board[0])

        # Function to check if `word` or its reverse can fit into `strWord`
        def isWordPlaceable(strWord, word):
            strWordLength = len(strWord)
            wordLength = len(word)
            
            if strWordLength != wordLength:
                return False

            # Check if `word` can match `strWord` directly
            tracker = 0
            for index in range(wordLength):
                if strWord[index] != word[index] and strWord[index] != " ":
                    break
                tracker += 1
            if tracker == wordLength:
                return True

            # Reset tracker and check if `word` matches `strWord` in reverse
            tracker = 0
            for index in range(wordLength):
                if strWord[index] != word[wordLength - index - 1] and strWord[index] != " ":
                    break
                tracker += 1
            if tracker == wordLength:
                return True
            
            return False

        # Check horizontally (rows)
        for col in range(colsLength):
            row = 0
            while row < rowsLength:
                # Skip any blocked cells
                while row < rowsLength and board[col][row] == "#":
                    row += 1
                strWord = ""
                # Collect characters until the next `#` or end of row
                while row < rowsLength and board[col][row] != '#':
                    strWord += board[col][row]
                    row += 1
                # Check if the collected string can place the word
                if strWord and isWordPlaceable(strWord, word):
                    return True

        # Check vertically (columns)
        for row in range(rowsLength):
            col = 0
            while col < colsLength:
                # Skip any blocked cells
                while col < colsLength and board[col][row] == "#":
                    col += 1
                strWord = ""
                # Collect characters until the next `#` or end of column
                while col < colsLength and board[col][row] != '#':
                    strWord += board[col][row]
                    col += 1
                # Check if the collected string can place the word
                if strWord and isWordPlaceable(strWord, word):
                    return True

        return False
