# https://leetcode.com/problems/majority-element/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Approach One
        n = len(nums)
        nums.sort()
        return nums[n//2]

        # Approach Two
        elementFrequency = defaultdict(int)
        for num in nums:
            elementFrequency[num] += 1

        n = len(nums)
        if n & 1:
            n = n + 1
        half = n // 2

        for key in elementFrequency:
            if elementFrequency[key] >= half: return key

        # Approach Thre
        count = 1
        candidate = nums[0]
        for i in range(1,len(nums)):
            if count == 0:
                candidate = nums[i]
                
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1

        return candidate
