class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # exactly one answer 
        # two numbers that add up to the target value 
        # you may not use the same element twice 
        
        # hashmap --> store the difference of each number and the target 
        # check through each number to see if they match teh difference 

        prevDiff = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in prevDiff:
                return [prevDiff[difference], i]
            else:
                prevDiff[n] = i