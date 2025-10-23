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

        temp, ans = [], [] # create a temo array and an answer array 

        def backtrack(): # create a helper function 
            if len(temp) == n: #check the base case, if the perm is full
                ans.append(temp[:])
                return # exit out 

            for x in nums: # iterate through each number 
                if x not in temp: # check if this number isnt in the temp array 
                    temp.append(x) # add it to the temp array 
                    backtrack() # create permutations
                    temp.pop() # pop the number so that it can reset for the next loop 
        backtrack() # initial trigger for the recursion 
        return ans # output answer 
