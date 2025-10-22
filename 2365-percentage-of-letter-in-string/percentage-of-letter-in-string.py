class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        # return percentage of characters that equal letter in s
        # rounded down to the nearest whole percent 


        # iterate through the string, check if character equals letter 
        # increment a count 
        # then i would divide by count by the length of the string 
        # round(2)

        count = 0 
        for item in s:
            if item == letter:
                count += 1
        return int(float(count)/float(len(s))*100)