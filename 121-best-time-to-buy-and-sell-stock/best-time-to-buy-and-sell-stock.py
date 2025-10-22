class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minP = float('inf')
        maxP = 0 
        for price in prices:
            if price < minP:
                minP = price 
            elif price-minP > maxP:
                maxP = price-minP
        return maxP