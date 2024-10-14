# https://leetcode.com/problems/roman-to-integer/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def romanToInt(self, s: str) -> int:

        # Approach One
        # romanNumbersMap = {
        #     "I" : 1,
        #     "V":  5,
        #     "X" : 10,
        #     "L" : 50,
        #     "C" : 100,
        #     "D" : 500,
        #     "M" : 1000
        # }

        # s = s.replace("IV", "IIII").replace("IX", "IIIIIIIII")
        # s = s.replace("XL", "XXXX").replace("XC", "XXXXXXXXX")
        # s = s.replace("CD", "CCCC").replace("CM", "CCCCCCCCC")

        # ans = 0
        # for eachRoman in s:
        #     ans += romanNumbersMap[eachRoman]
        # return ans

        # Approach Two
        # romanNumbersMap = {
        #     "I" : 1,
        #     "V":  5,
        #     "X" : 10,
        #     "L" : 50,
        #     "C" : 100,
        #     "D" : 500,
        #     "M" : 1000
        # }

        # ans = i = 0
        # n = len(s)
        # while i < n:
        #     if i < n-1 and s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
        #         ans += (romanNumbersMap[s[i+1]] - romanNumbersMap[s[i]])
        #         i += 2
        #     elif i < n-1 and s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
        #         ans += (romanNumbersMap[s[i+1]] - romanNumbersMap[s[i]])
        #         i += 2
        #     elif i < n-1 and s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
        #         ans += (romanNumbersMap[s[i+1]] - romanNumbersMap[s[i]])
        #         i += 2
        #     else:
        #         ans += romanNumbersMap[s[i]]
        #         i += 1
        # return ans

        # Approach Three
        # romanNumbersMap = {
        #     "I" : 1,
        #     "V":  5,
        #     "X" : 10,
        #     "L" : 50,
        #     "C" : 100,
        #     "D" : 500,
        #     "M" : 1000
        # }

        # ans = i = 0
        # n = len(s)
        # while i < n:
        #     if i < n-1 and romanNumbersMap[s[i]] < romanNumbersMap[s[i+1]]:
        #         ans += (romanNumbersMap[s[i+1]] - romanNumbersMap[s[i]])
        #         i += 2
        #     else:
        #         ans += romanNumbersMap[s[i]]
        #         i += 1
        # return ans

        # Approach Four
        romanNumbersMap = {
            "I" : 1,
            "V":  5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        ans = i = 0
        n = len(s)
        while i < n:
            if i < n-1 and s[i:i+2] in romanNumbersMap:
                ans += romanNumbersMap[s[i:i+2]] 
                i += 2
            else:
                ans += romanNumbersMap[s[i]]
                i += 1
        return ans

