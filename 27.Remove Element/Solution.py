class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c = 0
        for i in range(len(nums)):
            nums[i-c] = nums[i]
            if nums[i] == val:
                c+=1
        return len(nums)-c