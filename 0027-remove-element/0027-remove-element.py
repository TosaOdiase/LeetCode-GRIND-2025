class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #start with a pointer to go through array 
        k = 0
        #now need to iterate through the array using a for loop 
        for j in range(len(nums)):
            if nums[j] != val:
                nums[k] = nums[j]
                k += 1
        return k 