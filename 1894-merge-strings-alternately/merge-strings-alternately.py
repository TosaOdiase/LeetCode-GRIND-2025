class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = ''.join(a+b for a,b in zip(word1,word2))
        return merged + word2[len(word1):] + word1[len(word2):]
        