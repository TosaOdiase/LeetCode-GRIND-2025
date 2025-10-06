class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ans = ""
        for char in address:
            if char == '.':
                ans += ('[.]')
            else:
                ans += char
        return ans
