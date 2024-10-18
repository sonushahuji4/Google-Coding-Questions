# https://leetcode.com/problems/ransom-note/description/?envType=company&envId=google&favoriteSlug=google-six-months&difficulty=EASY&role=full-stack

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n1 = len(ransomNote)
        n2 = len(magazine)
        i = j = 0

        arr1 = sorted(ransomNote)
        arr2 = sorted(magazine)
        while i < n1 and j < n2:
            if arr1[i] == arr2[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i >= n1: return True
        return False
        
