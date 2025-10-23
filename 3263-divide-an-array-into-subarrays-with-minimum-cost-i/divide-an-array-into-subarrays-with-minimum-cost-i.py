class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # need the array to split into three 
        # get the first index to be a subarray 
        # find the next two lowest indexes and add them to total 
        x = nums[0]
        n = len(nums)
        nums[1:n] = sorted(nums[1:n])
        s = x + nums[1] + nums[2]
        return s