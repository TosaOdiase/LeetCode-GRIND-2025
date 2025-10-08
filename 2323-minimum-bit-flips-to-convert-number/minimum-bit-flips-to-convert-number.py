class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        x = bin(start ^ goal)[2:]
        count = 0
        for char in x:
            if char == '1':
                count += 1
        return count

        

        