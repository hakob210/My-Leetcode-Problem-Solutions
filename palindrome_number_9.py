class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0 and x == int(str(x)[::-1]):
            return True
        else:
            return False









sol = Solution()
res = sol.isPalindrome(12521)
print(res)
