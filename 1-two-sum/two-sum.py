class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # there is only one solution of indexes 
        # they need to add to the target value


        # create a difference variabel between the value and the target 
       # create a hash map to store previous differences

       # check if the difference is in the hash, if not then add the new diff to teh hash 
       # if it does excists, return that map index and the number index 

        prevDiff = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevDiff:
                return [prevDiff[diff], i]
            prevDiff[n] = i 
    