# https://leetcode.com/problems/maximum-split-of-positive-even-integers/description/

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0: return []
        maximumNumberOfIntegers, subtractiveCatalyst = [], 2
        while subtractiveCatalyst <= finalSum:
            maximumNumberOfIntegers += [subtractiveCatalyst]
            finalSum -= subtractiveCatalyst
            subtractiveCatalyst += 2
        maximumNumberOfIntegers[-1] += finalSum
        return maximumNumberOfIntegers
