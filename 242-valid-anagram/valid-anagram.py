class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False 
        countS, countT = {}, {}
        for i in range(len(s)):
            countT[s[i]] = 1 + countT.get(s[i], 0)
            countS[t[i]] = 1 + countS.get(t[i], 0)
        for num in countT:
            if countT.get(num,0) != countS.get(num,0):
                return False 
        return True
        