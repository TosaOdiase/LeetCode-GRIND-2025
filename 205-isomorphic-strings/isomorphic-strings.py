class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapAB, mapBA = {}, {}

        for i in range (len(s)):
            c1, c2 = s[i], t[i]
            if (c1 in mapAB and mapAB[c1] != c2) or (c2 in mapBA and mapBA[c2] != c1):
                return False
            mapAB[c1] = c2
            mapBA[c2] = c1
        return True




        