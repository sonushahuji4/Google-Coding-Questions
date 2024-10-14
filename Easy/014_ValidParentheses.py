# https://leetcode.com/problems/valid-parentheses/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []
        for char in s:
            if len(parentheses) > 0:
                if char == ')' and '(' == parentheses[-1]:
                    parentheses.pop()
                elif char == ']' and '[' == parentheses[-1]:
                    parentheses.pop()
                elif char == '}' and '{' == parentheses[-1]:
                    parentheses.pop()
                else:
                    parentheses += [char]
            else:
                parentheses += [char]
        if len(parentheses) == 0:
            return True
        return False
        
