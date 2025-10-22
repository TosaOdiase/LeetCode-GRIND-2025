class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # create a dictionary, with characters and their freqs 
        # check if lengths are equal 

        if len(s) != len(t):
            return False 
        
        count_t, count_s = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        for c in count_t:
            if count_t[c] != count_s.get(c, 0):
                return False
        return True
        