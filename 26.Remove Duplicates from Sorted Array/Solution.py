class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[c]:
                c+=1
                nums[c]=nums[i]
        return c+1