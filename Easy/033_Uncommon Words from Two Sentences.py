# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        # Approach One
        stMap = defaultdict(int)

        for word in s1.split(" "):
            stMap[word] += 1
           
        for word in s2.split(" "):
            stMap[word] += 1
        
        ans = []
        for key in stMap:
            if stMap[key] == 1:
                ans += [key]
        return ans
        
