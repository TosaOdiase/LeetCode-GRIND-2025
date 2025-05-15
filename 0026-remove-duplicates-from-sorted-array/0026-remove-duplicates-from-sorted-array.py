class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #worst case: theres no array 
        if not nums:
            return 0
        #in place means use a pointer and a loop 
        i = 0 
        #create a loop, but start the counter (j) at 1 instead of zero 
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

        
