# https://leetcode.com/problems/find-closest-number-to-zero/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

# Solution step-by-step
# 1. Divide the original list into two new lists: positives (p) and negatives (n).
# 2. If 0 is seen in the original list, immediately return 0.
# 3. If the positive list is empty we return the max value of the negatives.
# 4. If the negative list is empty we return the min value of the positives.
# 5. If both the negative and positive lists aren't empty, we check whether absolute max negative value is smaller than the absolute min postive value. If this is True we return the maximum negative value, if False we return the minimum positive value.

class Solution:
    def findClosestToZero(self, numbers: List[int]) -> int:
        # Separate positive and negative numbers
        positives = []
        negatives = []

        # Categorize the numbers into positives and negatives
        for num in numbers:
            if num == 0:
                return 0  # Return immediately if 0 is found
            elif num < 0:
                negatives.append(num)
            else:
                positives.append(num)
        
        # If no positive numbers, return the largest negative number (closest to zero)
        if not positives:
            return max(negatives)
        
        # If no negative numbers, return the smallest positive number (closest to zero)
        if not negatives:
            return min(positives)

        # Compare the absolute values of the largest negative and smallest positive numbers
        if abs(max(negatives)) < abs(min(positives)):
            return max(negatives)
        else:
            return min(positives)
