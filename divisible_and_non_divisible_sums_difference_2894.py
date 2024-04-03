class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        s = 0

        for i in range(n+1):
            if i % m != 0:
                s += i
            else:
                s -= i

        return s



sol = Solution()
res = sol.differenceOfSums(5, 1)
print(res)
