class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       # set a minimum price
       # set a max price 
        minP = float('inf')
        maxP = 0 
        for price in prices:
            if price < minP:
                minP = price
            else:
                profit = price - minP
                maxP = max(maxP,profit)
        return maxP



