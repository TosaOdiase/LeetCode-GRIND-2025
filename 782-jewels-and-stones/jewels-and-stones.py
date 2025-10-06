class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        check = set(jewels)
        ans = 0
        for rock in stones:
            if rock in jewels:
                ans += 1
        return ans 
