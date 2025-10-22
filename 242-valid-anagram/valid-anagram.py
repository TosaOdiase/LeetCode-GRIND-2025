from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        freq_t = Counter(t)
        freq_s = Counter(s)

        if freq_t == freq_s:
            return True 
        else:
            return False