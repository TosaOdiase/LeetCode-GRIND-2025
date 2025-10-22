class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        #only has sixes and nines 
        # only one change is allowed 
        # need the highest value 
        # highest value is going to be changing the leftmost six into a nine 
        
        # change the number into a list of characters
        # then i would have to iterate through characters, changing the first six to a nine 
        # i would then join the characters togetehr and convert to an integer 

        string = list(str(num))

        for i in range(len(string)):
            if string[i] == '6':
                string[i] = '9'
                break 
        ans = int("".join(string))
        return ans
        