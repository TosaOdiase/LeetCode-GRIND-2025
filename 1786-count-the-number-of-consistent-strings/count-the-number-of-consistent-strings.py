class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        rule = set(allowed)
        ans = 0 
        goodWord = False
        for word in words:
            for char in set(word):
                if char in rule:
                    goodWord = True
                else: 
                    goodWord = False
                    break
            if goodWord == True:
                ans+= 1 
        return ans

        