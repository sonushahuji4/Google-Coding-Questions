# https://leetcode.com/problems/climbing-stairs/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Solution:
    def climbStairs(self, n: int) -> int:

        # Approach One Recursion
        def distinctWays(n):
            if n == 0: return 1
            if n < 0: return 0
            stepOne = distinctWays(n-1)
            stepTwo = distinctWays(n-2)
            return stepOne + stepTwo
        return distinctWays(n)

        # Recursion + DP
        dp = [-1] * (n+1)
        def distinctWays(n):
            if n == 0: return 1
            if n < 0: return 0
            if dp[n] != -1: return dp[n]
            stepOne = distinctWays(n-1)
            stepTwo = distinctWays(n-2)
            dp[n] = stepOne + stepTwo
            return dp[n]
        return distinctWays(n)

        # Tabulation
        dp = [-1] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

        # Tabulation with Space Optimization
        stepOne = 1
        stepTwo = 1
        for i in range(2,n+1):
            currentStep = stepOne + stepTwo
            stepTwo = stepOne
            stepOne = currentStep
        return stepOne

        
