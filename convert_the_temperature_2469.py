class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        ans = [celsius + 273.15, celsius * 1.80 + 32]
        return ans





sol = Solution()
res = sol.convertTemperature(36.50)
print(res)
