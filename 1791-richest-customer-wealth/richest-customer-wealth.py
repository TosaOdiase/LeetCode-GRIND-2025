class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        rich = 0
        for customer in accounts:
            rich = max(sum(customer), rich)
        return rich 
        