class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i=0
        while(i>=0):
            if arr[i] != 0:
                i+=1
            else:
                arr.pop()
                arr.insert(i+1,0)
                i+=2
            if i>=len(arr):
                break
