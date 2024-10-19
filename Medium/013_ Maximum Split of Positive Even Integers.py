# https://leetcode.com/problems/maximum-split-of-positive-even-integers/description/

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        ansList, index = [], 2
        if finalSum % 2 == 0:
            while index <= finalSum:
                ansList += [index]
                finalSum -= index
                index += 2
            ansList[-1] += finalSum
        return ansList
