class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
  # min profit is zero 
  # buy date and a sell date 
  # buy date must come before your sell date 
        minPrice = float('inf')
        maxProfit = 0 
        for price in prices:
            minPrice = min(price, minPrice)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit