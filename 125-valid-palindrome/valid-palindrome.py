class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # without alpha numeric characters 
        # it has to reach the same forward and backward 
        # every character is lowercase 

        # create a new string for "fixed" string 
        # create a string that contains backwards iteration 
        # go through input, clean out non alpha, lowercase 
        # go backwards through this clean string, see if it equals the original clean string 

        clean = ""
        backward = ""

        for letter in s:
            if letter.isalpha():
                clean += letter.lower()
            elif letter.isdigit():
                clean += letter
        for item in reversed(clean):
            backward += item
        return backward == clean 