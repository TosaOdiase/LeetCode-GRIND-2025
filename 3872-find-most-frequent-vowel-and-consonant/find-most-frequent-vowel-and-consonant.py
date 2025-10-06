from collections import Counter 

class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        # create a set of vowels
        vowels = set('aeiou')
        # get a list of nouns and their frequency 
        freq = Counter(s)
        max_v = 0
        max_c = 0 

        for i, k in freq.items():
            if i in vowels:
                if k > max_v:
                    max_v = k
            else:
                if k > max_c:
                    max_c = k
        return max_c + max_v


