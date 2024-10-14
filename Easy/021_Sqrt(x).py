# https://leetcode.com/problems/sqrtx/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = low + (high - low)//2
            sqrRoot = mid * mid
            if sqrRoot == x: return mid
            elif sqrRoot > x: 
                high = mid - 1
            else:
                low = mid + 1
        return high
        
