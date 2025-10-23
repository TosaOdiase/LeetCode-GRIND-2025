class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # recursion probelm 
        # result, list of arrays with all permutations 
        # need helper function to split subarrays and add to elements, and pop one that are not needed 

        n = len(nums)
        ans, temp = [], []

        def backtrack():
            if len(temp) == n:
                ans.append(temp[:])
                return 
            for x in nums:
                if x not in temp:
                    temp.append(x)
                    backtrack()
                    temp.pop()
        backtrack()
        return ans
        