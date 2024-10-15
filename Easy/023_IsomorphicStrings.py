# https://leetcode.com/problems/isomorphic-strings/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # Approach One
        sLength = len(s)
        tLength = len(t)
        if sLength != tLength: return False

        sHashMap = dict()
        tHashMap = dict()
        for index in range(sLength):
            sChar = s[index]
            tChar = t[index]

            if sChar in sHashMap:
                if sHashMap[sChar] != tChar: return False
            elif tChar in tHashMap:
                if tHashMap[tChar] != sChar: return False
            else:
                sHashMap[sChar] = tChar
                tHashMap[tChar] = sChar
        return True
