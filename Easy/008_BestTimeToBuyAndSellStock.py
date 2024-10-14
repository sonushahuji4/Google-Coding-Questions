# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Approach One Time Complexity O(n^2)
        pricesLength = len(prices)
        maxProfit = 0
        for i in range(pricesLength):
            buyingPrice = prices[i]
            for j in range(i+1,pricesLength):
                sellingPrice = prices[j]
                maxProfit = max(maxProfit, sellingPrice - buyingPrice)
        return maxProfit
        

        # Approach Two One Time Complexity O(n)
        pricesLength = len(prices)
        prefixBuyPrices = [0] * pricesLength
        prefixBuyPrices[0] = prices[0]
        for i in range(1,pricesLength):
            prefixBuyPrices[i] = min(prefixBuyPrices[i-1], prices[i])
        
        maxProfit = 0
        for i in range(pricesLength):
            maxProfit = max(maxProfit, prices[i] - prefixBuyPrices[i])
        return maxProfit

        # Approach Three
        pricesLength = len(prices)
        buyingPrice = prices[0]
        sellingPrice = 0
        for i in range(1,pricesLength):
            # can i buy at cheaper rate ?
            if buyingPrice > prices[i]:
                buyingPrice = prices[i]
            if buyingPrice < prices[i]:
                sellingPrice = max(sellingPrice,prices[i] - buyingPrice)
            # how much profit do i make
        return sellingPrice
       
