class Solution(object):
    def thirdMax(self, nums):
        l=-2**31
        s=-2**31
        t=-2**31
        for i in nums:
            if i>l :
                t=s
                s=l
                l=i
            elif i>s and  i<l :
                t=s
                s=i
            elif i>t and i<s:
                t=i
            else:
                continue  
        if min(nums)==s or min(nums)==l:
            return l
        return t