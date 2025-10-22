class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # must have three subarray 
        # must find the minimum
        # first number in subarray is the value 

        # after the first, must find the two lowest numbers to start at 

        # create a best value 

        #exclude the first index 
        n = len(nums)
        d = nums[0]

        # sort the rest, to get the two lowest in front 

        nums[1:n] = sorted(nums[1:n])

        ans = d + nums[1] + nums[2]
        return ans

        