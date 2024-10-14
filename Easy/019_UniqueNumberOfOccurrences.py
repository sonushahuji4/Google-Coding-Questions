# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        for num in arr:
            freq[num] += 1
        occurs = set()
        for key in freq:
            if freq[key] not in occurs:
                occurs.add(freq[key])
                continue
            return False
        return True
        
