class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ""

        dp = [[False] * n for _ in range(n)]

        max_length = 1
        start_index = 0
        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                max_length = 2
                start_index = i

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_length:
                        max_length = length
                        start_index = i

        return s[start_index:start_index + max_length]







sol = Solution()
res = sol.longestPalindrome("do dododo hananabananah bubu e")
print(res)
