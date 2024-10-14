# https://leetcode.com/problems/palindrome-number/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Approach One (Two Pointer)
        nums = [num for num in str(x)]
        low, high = 0, len(nums)-1

        while low <= high:
            if nums[low] != nums[high]: return False
            low += 1
            high -= 1
        return True

        # Approach Reverse the nums and check equal or not
        if x < 0: return False
        reverseNums = []
        reminder = 0
        num = x
        while num > 0:
            reminder = num%10
            num = num//10
            reverseNums.append(reminder)
        
        return reverseNums == reverseNums[::-1]

        # Approach Three
        return str(x)==str(x)[::-1]
