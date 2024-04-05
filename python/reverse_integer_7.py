class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        max_int = 2**31 - 1
        min_int = -2**31
        
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1
        
        r = 0
        while x:
            if r > max_int // 10 or r < min_int // 10:
                return 0
            r = r * 10 + x % 10
            x = x // 10
        return sign * r





sol = Solution()
res = sol.reverse(-12345)
print(res)
