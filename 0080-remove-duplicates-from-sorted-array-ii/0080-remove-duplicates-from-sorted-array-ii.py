class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        # okay you need a pointer for in place, this will be two ahead 
        i = 2 
        #then you need a loop to match 
        for j in range(2, len(nums)):
            #checks if the posttion two positions ahead matches
            if nums[j] != nums[i-2]:
                #appends when it is unique 
                nums[i] = nums[j]
                i += 1
        return i 



