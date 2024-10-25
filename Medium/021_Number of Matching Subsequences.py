# https://leetcode.com/problems/number-of-matching-subsequences/description/

# Approach One

from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        result = defaultdict(str)
        n = len(s)
        def subq(arr,i):
            if i >= n:
                result[arr] = True
                return 
            subq(arr + s[i], i + 1)
            subq(arr, i + 1)
        subq("", 0)
        
        count = 0
        for word in words:
            if result[word]:
                count += 1

        return count


# Approach Two


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        sLength = len(s)
        for word in words:
            i = j = 0
            wordLength = len(word)
            while i < wordLength and j < sLength:
                if word[i] == s[j]:
                    i += 1
                j += 1
            if i == wordLength:
                count += 1
        return count
                



# Approach Three

from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        sLength = len(s)
        mapWords = defaultdict(int)
        for word in words:
            mapWords[word] += 1

        for word, frequency in mapWords.items():
            i = j = 0
            wordLength = len(word)
            while i < wordLength and j < sLength:
                if word[i] == s[j]:
                    i += 1
                j += 1
            if i == wordLength:
                count += frequency
        return count
