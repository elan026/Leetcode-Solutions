class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = 0
        temp = x
        while(x > 0):
            rev = rev * 10 + x % 10
            x = x//10
        if rev == temp:
            return True
        else:
            return False


        