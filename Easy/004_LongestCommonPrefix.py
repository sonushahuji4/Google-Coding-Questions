# https://leetcode.com/problems/longest-common-prefix/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Approach One
        # strsLenght = len(strs)
        # if strsLenght == 0: return ""

        # # Initialize the prefix with the first string
        # ans = strs[0]
        # ansLength = len(ans)

        # # Start from the second string and compare with the prefix
        # for i in range(1, strsLenght):
        #     while ans[:ansLength] != strs[i][:ansLength]:
        #         ansLength -= 1
        #         if ansLength == 0:
        #             return ""
        # return ans[:ansLength] if len(strs) > 1 else strs[0]

        # Approach Two
        # ans = ''
        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i == len(s) or s[i] != strs[0][i]:
        #             return ans
        #     ans += strs[0][i]
        # return ans

        # Approach Three
        # if len(strs) == 0: return ''
        # if len(strs) == 1: return strs[0]

        # Sort the list to compare only the first and last strings
        # After sorting, the longest common prefix must exist in the first and last strings of the sorted list 
        # because these strings will have the least and most differing prefixes, respectively.
        # strs.sort()
        # ans = ''
        # minLen = min(len(strs[0]), len(strs[1]))
        # for i in range(minLen):
        #     if strs[0][i] == strs[1][i]:
        #         ans += strs[0][i]
        # return ans

        # Approach Four
        strsLength = len(strs)
        if strsLength == 0: return ""

        minLengthWord = 10**9+7
        for eachWord in strs:
            minLengthWord = min(minLengthWord, len(eachWord))
        
        def isCommonPrefix(strs, l):
            str1 = strs[0][:l]
            for i in range(1, len(strs)):
                if not strs[i].startswith(str1):
                    return False
            return True

        low, high = 1, minLengthWord
        while low <= high:
            mid = low + (high - low) // 2
            if isCommonPrefix(strs, mid):
                low = mid + 1
            else:
                high = mid - 1
        return strs[0][0:(low + high) // 2]

        
