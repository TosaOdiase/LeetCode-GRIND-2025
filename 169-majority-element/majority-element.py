class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Create a counter  
        count = 0 
        #Create a candidate 
        candidate = None
        # Loop for all elements 
        for num in nums:
            if count == 0:
                candidate = num 
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate 


        