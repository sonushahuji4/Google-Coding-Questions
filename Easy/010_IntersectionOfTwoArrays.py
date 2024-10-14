# https://leetcode.com/problems/intersection-of-two-arrays/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Approach One
        uniNum1 = set(nums1)
        uniNum2 = set(nums2)
        intersectionElement = []
        for num1 in uniNum1:
            for num2 in uniNum2:
                if num1 == num2:
                    intersectionElement += [num1]
                    break
        return intersectionElement

        # Approach Two
        uniNum1 = set(nums1)
        uniNum2 = set(nums2)
        return list(uniNum1 & uniNum2)

        # Approach Three
        nums1.sort()
        nums2.sort()

        nums1Length = len(nums1)
        nums2Length = len(nums2)

        firstPointer = secondPointer = 0
        intersection = set()

        while firstPointer < nums1Length and secondPointer < nums2Length:
            if nums1[firstPointer] == nums2[secondPointer]:
                intersection.add(nums1[firstPointer])
                firstPointer += 1
                secondPointer += 1
            elif nums1[firstPointer] < nums2[secondPointer]:
                firstPointer += 1
            else:
                secondPointer += 1
        
        intersectionPoints = []
        for point in intersection:
            intersectionPoints.append(point)

        return intersectionPoints
        
        # Approach Four
        intersection = dict()
        for num in nums1:
            intersection[num] = 1
           
        intersectionPoints = []
        for num in nums2:
            if num in intersection and intersection[num] == 1:
                intersectionPoints += [num]
                intersection[num] = 0

        return intersectionPoints
