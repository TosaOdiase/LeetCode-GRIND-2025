class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """


        # the max acheivable has to be t*2 steps away, in order to be able to achieve num

        x = num + t*2
        return x