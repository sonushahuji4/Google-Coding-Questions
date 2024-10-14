# https://leetcode.com/problems/merge-sorted-array/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        # Brute Force Approach O(n + m)log(n + m)
        
        # for i in range(n):
        #     nums1[m + i] = nums2[i]
        # nums1.sort()


        # Better Approach O(m + n) but this takes extra space
        
        # copyNums = []
        # i = j = 0
        # while i < m and j < n:
        #     if nums1[i] <= nums2[j]:
        #         copyNums.append(nums1[i])
        #         i += 1
        #     else:
        #         copyNums.append(nums2[j])
        #         j += 1
        
        # while i < m:
        #     copyNums.append(nums1[i])
        #     i += 1
        
        # while j < n:
        #     copyNums.append(nums2[j])
        #     j += 1
        
        # for k in range(m+n):
        #     nums1[k] = copyNums[k]


        # Optimal Approach

        mPointer = m - 1
        nPointer = n - 1
        lastPointer = (m + n) - 1

        # Merge nums1 and nums2 from the end
        while mPointer >= 0 and nPointer >= 0:
            if nums2[nPointer] > nums1[mPointer]:
                nums1[lastPointer] = nums2[nPointer]
                nPointer -= 1
            else:
                nums1[lastPointer] = nums1[mPointer]
                mPointer -= 1
            lastPointer -= 1

        # If there are leftover elements in nums2, copy them to nums1
        while nPointer >= 0:
            nums1[lastPointer] = nums2[nPointer]
            nPointer -= 1
            lastPointer -= 1


