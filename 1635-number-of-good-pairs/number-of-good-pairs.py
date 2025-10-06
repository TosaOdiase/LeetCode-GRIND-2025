class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pair = {}
        ans = 0
        for num in nums:
            pair[num] = pair.get(num,0) + 1
        for val in pair.values():
            ans += val*(val-1)/2
        return ans
            