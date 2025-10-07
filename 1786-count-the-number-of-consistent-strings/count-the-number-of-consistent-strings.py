class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        rules = set(allowed)
        ans = 0 
        for word in words:
                if all(char in rules for char in word):
                    ans+= 1 
        return ans
        