class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans = 0 
        
        for char in operations:
            if char == "--X" or char == "X--":
               ans = ans - 1
            elif char == "++X" or char == "X++":
                ans = ans + 1
        return ans
        