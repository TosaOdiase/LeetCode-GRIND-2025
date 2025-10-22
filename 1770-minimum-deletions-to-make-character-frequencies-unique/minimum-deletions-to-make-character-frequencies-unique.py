from collections import Counter
class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # diff levels of freq 
        # only decrement 
        # need the minimal deletions 
        # freqs will have to be above zero to be comparable 

        #plan 
        # get the freq of each character 
        # value for deletions 
        # create a set for known freq values 

        # check if freq is alr used, decrement if so, add to alr used if not 
        # when i decrement, i will lower the freq, and then i will increase the amount of deletions

        freq = Counter(s)
        deletions = 0 
        used = set()

        for i in freq.values():
            while i > 0 and i in used:
                deletions += 1
                i -= 1
            if i > 0:
                used.add(i)
        return deletions

