class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # set the length of the nums 
        # create a temp array, and a result array 

        # create backtrack function 
        # base case: if temp == length of the num, return a copy of the solution 
        # iterate through the numbers 
        # append the current number
        # run teh backtrcak function to add permutations to sol
        # pop the number that you added on orriginallty 

        #run backtrack, the inital trigger 

        n = len(nums)

        temp, ans = [], []

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
