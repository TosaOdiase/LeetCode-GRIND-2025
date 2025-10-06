class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            if num % 2 == 0:
                ans.append(0)
            else:
                ans.append(1)
        ans.sort()
        return ans
        