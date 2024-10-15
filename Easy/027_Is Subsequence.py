# https://leetcode.com/problems/is-subsequence/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        Approach One
        n = len(t)

        def isSubSq(i,subSet):
            if i >= n:
                if s == subSet: return True
                return False
            
            left = isSubSq(i + 1, subSet + t[i])
            if left: return True
            right = isSubSq(i + 1, subSet)
            return left or right
        return isSubSq(0, '')

        # Approach Two
        sLength = len(s)
        tLength = len(t)
        sPointer = tPointer = countChar = 0
        while sPointer < sLength and tPointer < tLength:
            if s[sPointer] == t[tPointer]:
                countChar += 1
                sPointer += 1
                tPointer += 1
            else:
                tPointer += 1
        return sLength == countChar

        
