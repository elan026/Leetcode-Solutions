class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # a = sorted(nums)
        # e , o = 0 , 1
        # for i in nums:
        #     if i%2==0:
        #         a[e]=i
        #         e+=2
        #     else:
        #         a[o]=i
        #         o+=2
        # return a

        a = [0]*len(nums)
        e , o = 0 , 1
        for i in nums:
            if i%2==0:
                a[e]=i
                e+=2
            else:
                a[o]=i
                o+=2
        return a