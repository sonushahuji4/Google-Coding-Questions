# https://leetcode.com/problems/largest-odd-number-in-string/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        # Approach One
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) & 1 != 0:
                return num[:i+1]
        return ""
        
