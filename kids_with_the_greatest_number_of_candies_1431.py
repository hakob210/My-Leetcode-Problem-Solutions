class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        booleans = []

        for kid in candies:
            n = candies[:]
            n.append(kid + extraCandies)
            booleans.append(max(n) == kid + extraCandies)

        return booleans










sol = Solution()
res = sol.kidsWithCandies([2, 3, 5, 1, 3], 3)
print(res)
