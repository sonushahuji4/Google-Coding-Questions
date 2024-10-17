# https://leetcode.com/problems/sort-integers-by-the-power-value/description/

import heapq

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        def getPowerOfX(x):
            if x % 2 == 0:
                return x//2
            else:
                return (3*x+1)

        minHeap = []
        while lo <= hi:
            num = lo
            count = 0
            while num != 1:
                count += 1
                num = getPowerOfX(num)
            heapq.heappush(minHeap,(count,lo))
            lo += 1
        
        num = steps = 0
        while k > 0:
            steps, num = heapq.heappop(minHeap)
            k -=1
        return num
