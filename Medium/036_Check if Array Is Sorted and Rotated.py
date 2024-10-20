# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/?envType=company&envId=google&favoriteSlug=google-six-months&difficulty=EASY&role=full-stack

class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(len(nums)):
            if nums[i-1] > nums[i]:
                cnt += 1
        if cnt <= 1: return True
        return False     
