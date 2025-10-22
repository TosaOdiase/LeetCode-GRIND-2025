class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        #integer only consists of 6s and 9 
        # only change one 
        # max value 

        #change the leftmost 6 into a 9 
        # turn the number into a list of strings 

        # then i will iterate through the string and replace the first 6 with a 9 
        # convert back to an integer 

        numbers = list(str(num))

        for i in range(len(numbers)):
            if numbers[i] == "6":
                numbers[i] = "9"
                break 
        ans = "".join(numbers)
        return int(ans)