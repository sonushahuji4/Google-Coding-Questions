# https://leetcode.com/problems/valid-palindrome/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Approach One
        sentenceString = ""
        for char in s:
            ch = ord(char)
            if  ord('a') <= ch <= ord('z'):
                sentenceString += char
            elif ord('A') <= ch <= ord('Z'):
                sentenceString += char.lower()
            elif char in ['0','1','2','3','4','5','6','7','8','9']:
                sentenceString += char

        
        n = len(sentenceString)
        leftPointer, rightPointer = 0, n - 1

        while leftPointer < rightPointer:
            if sentenceString[leftPointer] != sentenceString[rightPointer]:
                return False
            leftPointer += 1
            rightPointer -= 1
        return True

        # Approach Two
        sentenceString = ""
        for char in s:
            ch = ord(char)
            if  ord('a') <= ch <= ord('z'):
                sentenceString += char
            elif ord('A') <= ch <= ord('Z'):
                sentenceString += char.lower()
            elif char in ['0','1','2','3','4','5','6','7','8','9']:
                sentenceString += char
        
        return sentenceString == sentenceString[::-1]



        
