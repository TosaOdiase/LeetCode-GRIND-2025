class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        count = 0 

        for k in s:
            if k == letter:
                count += 1
        return int(count/float(len(s))*100)