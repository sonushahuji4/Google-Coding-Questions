# https://leetcode.com/problems/merge-strings-alternately/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # Approach One (Two Pointer)
        word1Length = len(word1)
        word2Length = len(word2)
        w1 = w2 = 0
        alternativeStrings = ""
        while w1 < word1Length and w2 < word2Length:
            alternativeStrings += word1[w1]
            alternativeStrings += word2[w2]
            w1 += 1
            w2 += 1
        
        while w1 < word1Length:
            alternativeStrings += word1[w1]
            w1 += 1
        
        while w2 < word2Length:
            alternativeStrings += word2[w2]
            w2 += 1

        return alternativeStrings


        # Approach Two (One Pointer)
        lenghtOfWord1 = len(word1)
        lenghtOfWord2 = len(word2)
        maxLengthOfWord = max(lenghtOfWord1, lenghtOfWord2)
        mergedStringResult = ""
        
        for i in range(maxLengthOfWord):
            if i < lenghtOfWord1:
                mergedStringResult += word1[i]
            if i < lenghtOfWord2:
                mergedStringResult += word2[i]

        return mergedStringResult
