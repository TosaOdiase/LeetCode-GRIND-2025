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
        best = 3000

        for i in range(1, len(nums)):
            for j in range(i+1,len(nums)):
                best = min(best, nums[0] + nums[i] + nums[j])
        return best


        