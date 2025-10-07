class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        y,m,d = date.split("-")
        y = bin(int(y))[2:]
        m = bin (int(m))[2:]
        d = bin(int(d))[2:]
        return '-'.join([y,m,d])