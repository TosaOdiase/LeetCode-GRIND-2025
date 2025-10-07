class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        new = date.split('-')
        ans = []
        for word in new:
            ans.append(bin(int(word))[2:])
        return '-'.join(ans)
