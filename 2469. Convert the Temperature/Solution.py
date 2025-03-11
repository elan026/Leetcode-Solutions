class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        ans = []
        k = celsius + 273.15
        f = celsius * 1.80 + 32.00
        ans.append(k)
        ans.append(f)
        return ans