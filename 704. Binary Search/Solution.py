class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if target in nums:
        #     return nums.index(target)
        # return -1

        mid=0
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)/2
            num=nums[mid]
            if(num==target):
                return mid
            if target<num:
                high=mid-1
            if target>num:
                low=mid+1
        return -1
        