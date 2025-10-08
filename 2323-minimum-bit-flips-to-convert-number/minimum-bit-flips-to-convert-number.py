class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        x = start ^ goal
        y = str(bin(x))
        count = 0
        for char in y[2:]:
            if char == '1':
                count += 1
        return count

        

        