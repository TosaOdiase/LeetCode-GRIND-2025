class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # create an array, all values add to zero 
        # all values need to be unique 
        # you can use neg values and pos 
        # you can use zero 

        # intialize the array 
        ans = []
        # check if the array length is even or odd
        if n % 2 == 0:
            for i in range(1, n/2 + 1):
                ans.append(i)
                ans.append(i*-1)
        else:
            for i in range(1, (n - 1) / 2 + 1):
                ans.append(i)
                ans.append(i*-1)
            ans.append(0)
        return ans

    

        
        