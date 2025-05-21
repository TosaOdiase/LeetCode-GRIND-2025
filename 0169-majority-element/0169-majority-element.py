class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counter 
        count = 0 
        # then select a canidate element
        canidate = None 
        #for loop all elements
        for num in nums:
            if count == 0:
                canidate = num
            if canidate == num: 
                count += 1
            else: 
                count -= 1
        return canidate  
