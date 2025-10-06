class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        if len(friends) > len(order):
            return friends 
        ans = []
        for person in order:
            if person in friends:
                ans.append(person)
        return ans 
