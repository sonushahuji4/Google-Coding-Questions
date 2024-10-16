# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a,b):
            if b == 0: 
                return a
            else:
                return gcd(b, a%b)

        if str1 + str2 != str2 + str1: return ""
        maxLenght = gcd(len(str1), len(str2))
        return str1[:maxLenght]
