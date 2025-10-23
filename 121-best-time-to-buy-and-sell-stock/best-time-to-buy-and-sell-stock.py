class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minP = float('inf')
        maxProfit = 0 

        for price in prices:
            if price < minP:
                minP = price
            if price - minP > maxProfit:
                maxProfit = price - minP
        return maxProfit
        