class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #initialize a hashmap 
        hashmap = {}

    #creates the index with values and keys
        for i,num in enumerate(nums):
            # creates the diff 
            diff = target - num 
            #checks if the difference is in the hmap
            if diff in hashmap:
                # returns the index value and the index of the diff in hmap
                return [i,hashmap[diff]]
            #initilizes the value at the location i 
            hashmap[num] = i
           



        