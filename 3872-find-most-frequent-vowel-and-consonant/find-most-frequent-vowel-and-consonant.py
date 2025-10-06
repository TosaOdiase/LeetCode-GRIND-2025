class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """

        vowels = set('aeiou')
        v = {}
        c = {}

        for ch in s:
            if ch in vowels:
                v[ch] = v.get(ch,0) + 1
            else:
                c[ch] = c.get(ch,0) + 1
        
        maxv = max(v.values()) if v else 0
        maxc = max(c.values()) if c else 0
        return maxv + maxc

        



        