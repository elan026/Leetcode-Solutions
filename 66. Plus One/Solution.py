class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ""
        for i in range(len(digits)):
            s += str(digits[i])
        s = str(int(s)+1)
        digit=[]
        for i in s:
            digit.append(int(i))
        return digit