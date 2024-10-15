# https://leetcode.com/problems/range-sum-query-immutable/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack


# Approach One
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = self.prefixSumCaculate(nums)

    
    def prefixSumCaculate(self,nums) -> List[int]:
        numsLength = len(nums)
        prefixSum = ([0] * numsLength)
        prefixSum[0] = nums[0]
        for i in range(1,numsLength):
            prefixSum[i] = nums[i] + prefixSum[i-1]
        return prefixSum
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        else:
            return self.prefixSum[right] - self.prefixSum[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
