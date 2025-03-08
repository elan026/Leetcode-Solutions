class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        s1 = 1
        s2 = 1
        for i in range(2,n+1):
            a = s1+s2
            s2 = s1
            s1 = a
        return s1