# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR to find differing bits
        xor_result = start ^ goal
        count = 0
        # Brian Kernighans algorithm to count 1s
        while xor_result:
            xor_result &= xor_result - 1  # Clear the lowest set bit
            count += 1
        return count
