class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        for i in range(0,len(candies)):
            result.append((candies[i]+extraCandies) >= max(candies))
        return result
        