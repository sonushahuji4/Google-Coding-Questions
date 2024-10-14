# https://leetcode.com/problems/valid-anagram/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Approach One
        sSorted = sorted(s)
        tSorted = sorted(t)
        return sSorted == tSorted

        # Approach Two
        if len(s) != len(t): return False
        charFrequencyTracker = dict()
        for ch in s:
            if ch in charFrequencyTracker:
                charFrequencyTracker[ch] += 1
            else:
                charFrequencyTracker[ch] = 1
        
        for ch in t:
            if ch in charFrequencyTracker:
                charFrequencyTracker[ch] -= 1
            else:
                charFrequencyTracker[ch] = 1

        isAngram = True
        for key in charFrequencyTracker:
            if charFrequencyTracker[key] != 0: return False
        return isAngram
