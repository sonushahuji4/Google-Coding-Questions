# https://leetcode.com/problems/power-of-four/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        # Approach One
        if n == 1: return True
        while n:
            if n == 1: return True
            elif n % 4 == 0:
                n = n//4
            else:
                return False
        
        # Approach Two
        while n % 4 == 0:
            n = n // 4
        if n == 1: return True
        return False

        # Approach Three
        if n > 0 and (n & (n-1)) == 0: 
            return (n -1) % 3 == 0
        return False
        
