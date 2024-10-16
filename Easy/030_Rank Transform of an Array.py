# https://leetcode.com/problems/rank-transform-of-an-array/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        # Approach One
        numToRank = dict()
        sortedArr = sorted(arr)
        rank = 1
        arrLength = len(arr)
        for i in range(arrLength):
            if i > 0 and sortedArr[i] > sortedArr[i-1]:
                rank += 1
            numToRank[sortedArr[i]] = rank

        for i in range(arrLength):
            arr[i] = numToRank[arr[i]]
        return arr     
