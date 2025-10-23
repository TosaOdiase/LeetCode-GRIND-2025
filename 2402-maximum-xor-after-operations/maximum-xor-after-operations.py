class Solution(object):
    def maximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0 
        for x in nums:
            ans |= x
        return ans
            