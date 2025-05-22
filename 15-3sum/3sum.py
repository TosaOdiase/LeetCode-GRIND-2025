class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            right, left = len(nums) - 1, i+1 
            while left < right:
                sum = nums[i] + nums[right] + nums[left]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[right], nums[left]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1 
                    while left <right and nums[right] == nums[right -1]:
                        right -= 1 
                    left += 1 
                    right -= 1
        return answer
                

                   
        
        
            


