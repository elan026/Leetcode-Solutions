class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        mi = -2**31
        ma = 2**31 - 1
        rev = 0
        temp = x
        if x<0:
            x=-(x)
        while(x):
            y = x%10
            rev=rev*10+y
            if mi > rev or ma < rev:
                return 0
            x=x//10
        if temp < 0:
            return -(rev)
        return rev