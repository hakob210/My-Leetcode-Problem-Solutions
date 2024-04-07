class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        s = 0
        alts = [0]
        for i in range(0, len(gain)):
            s += gain[i]
            alts.append(s)

        return max(alts)





sol = Solution()
res = sol.largestAltitude([-5, 1, 5, 0, -7])
print(res)
