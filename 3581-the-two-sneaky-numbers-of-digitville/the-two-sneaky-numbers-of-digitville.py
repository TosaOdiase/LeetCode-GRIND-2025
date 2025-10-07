class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        h = {}
        ans = []
        for num in nums:
            h[num] = h.get(num, 0) + 1
            if h[num] > 1:
                ans.append(num)
        return ans

        