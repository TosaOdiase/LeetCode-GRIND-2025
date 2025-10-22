class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # return amount of numbers 
        # must add up to zero 
        # can include zero 

        # even n values, append pos and negative values 
        # odd n values, we can add an extra zero 

        ans = []
        if n % 2 == 1:
            ans.append(0)
            n -= 1
        for i in range(1, (n/2) + 1):
            ans.append(i)
            ans.append(i*-1)
        return ans

        