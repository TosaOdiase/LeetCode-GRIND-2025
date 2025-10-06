class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        first = abs(x-z)
        second = abs(y-z)

        if first > second:
            return 2
        elif second > first:
            return 1
        else:
            return 0