# https://leetcode.com/problems/sort-integers-by-the-power-value/description/

import heapq

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        # Approach One
        def getPowerOfX(x):
            steps = 0
            while x != 1:
                if x % 2 == 0:
                    x = x//2
                else:
                    x = (3*x+1)
                steps += 1
            return steps
                
        
        minHeap = []
        while lo <= hi:
            count = getPowerOfX(lo)
            heapq.heappush(minHeap,(count,lo))
            lo += 1
        
        num = steps = 0
        while k > 0:
            steps, num = heapq.heappop(minHeap)
            k -=1
        return num

        # Approach Two
        dp = dict()
        def getPowerOfX(x):
            if x in dp: return dp[x]
            if x == 1: return 0
            if x%2 == 0:
                dp[x] = 1 + getPowerOfX(x//2)
            else:
                dp[x] = 1 + getPowerOfX(3 * x +1)
            return dp[x]

        minHeap = []
        while lo <= hi:
            count = getPowerOfX(lo)
            heapq.heappush(minHeap,(count,lo))
            lo += 1
        
        num = steps = 0
        while k > 0:
            steps, num = heapq.heappop(minHeap)
            k -=1
        return num
