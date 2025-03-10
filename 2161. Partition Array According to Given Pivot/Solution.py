class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        # j=0
        # n=deque([])
        # for i in range(len(nums)):
        #     if nums[i] >pivot:
        #         n.append(nums[i])
        #     else:
        #         n.appendleft(nums[i])
        # return sorted(list(n))

        a,b,c=[],[],[]
        for i in nums:
            if i < pivot:
                a.append(i)
            elif i == pivot:
                b.append(i)
            else:
                c.append(i)
        return a+b+c