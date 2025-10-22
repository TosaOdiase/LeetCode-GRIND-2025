class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # maek a dictionary to store all of the letter formations 
        # iterate through each word, reorganize caharcters, create matches 
        # append similar words to the same dictionary index 
        # append next set at their own index 
        # return a list of all values at every index of my dictionary 
        
        # dict 
        group = {}
        # iteration 
        for word in strs:
            # normalize characters 
            unique = "".join(sorted(word))
            if unique in group:
                group[unique].append(word)
            else:
                group[unique] = [word]
        return list(group.values())