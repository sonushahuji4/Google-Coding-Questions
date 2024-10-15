# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def reverseVowels(self, s: str) -> str:

        # Approach One
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        colloectedVowels = []
        for ch in s:
            if ch in vowels:
                colloectedVowels.append(ch)
        i = len(colloectedVowels) - 1
        ans = ""
        for ch in s:
            if ch in vowels:
                ans += colloectedVowels[i]
                i -= 1
            else:
                ans += ch
        return ans

        # Approach Two
        sLength = len(s)
        low, high = 0, sLength - 1
        vowels = set('aeiouAEIOU')
        ans = list(s)
        while low <= high:
            isLowVowel = ans[low] in vowels
            isHighVowel = ans[high] in vowels
            if isLowVowel and isHighVowel:
                ans[low], ans[high] = ans[high], ans[low]
                low += 1
                high -= 1
            if not isLowVowel:
                low += 1
            if not isHighVowel:
                high -= 1
        return ''.join(ans)
            
        
