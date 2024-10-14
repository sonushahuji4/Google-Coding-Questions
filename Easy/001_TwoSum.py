# https://leetcode.com/problems/two-sum/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Brute force solution O(n^2)
        
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] == target: return [i,j]
        
        # Better solution O(nlog) (This solution will not work since index matter here, sorting changes the index when you return)
        
        # nums.sort()
        # n = len(nums)
        # leftPointer = 0
        # rightPointer = n-1
        # while leftPointer < rightPointer:
        #     total = nums[leftPointer] + nums[rightPointer]
        #     if total == target: return [leftPointer, rightPointer]
        #     elif total < target:
        #         leftPointer += 1
        #     else:
        #         rightPointer -= 1

        # Optimal Solution O(n)

        trackBElement = dict()
        n = len(nums)
        for i in range(n):
            bElement = target - nums[i]
            if bElement in trackBElement: return [i, trackBElement[bElement]]
            else:
                trackBElement[nums[i]] = i



        
