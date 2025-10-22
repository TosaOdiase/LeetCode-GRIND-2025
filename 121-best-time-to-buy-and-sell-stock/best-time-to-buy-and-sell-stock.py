class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # track our buy day and our sell day 
        # our buy day must be before our sell day 
        # need to buy at the minmum, sell at the max

        l = 0 
        r = 1
        maxProfit = 0 

        while r < len(prices):
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r 
            r += 1
        return maxProfit