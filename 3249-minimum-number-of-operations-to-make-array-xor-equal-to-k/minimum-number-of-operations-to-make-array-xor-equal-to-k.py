class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # zero index int array 
        
        # find xor or all array elements
        # find x between that final xor and k 
        # count the amount of 1s in the binary set of that result 
        finalXor = 0
        for num in nums:
            finalXor = finalXor ^ num
        finalXor = finalXor ^ k 

        return bin(finalXor).count('1')
        