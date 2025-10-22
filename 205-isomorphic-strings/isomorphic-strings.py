class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapAB, mapBA = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if mapAB.get(c1) != mapBA.get(c2):
                return False
            mapAB[c1] = i
            mapBA[c2] = i
        return True