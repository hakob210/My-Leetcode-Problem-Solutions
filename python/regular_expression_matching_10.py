class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memory = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        memory[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == '.')

                if j + 1 < len(p) and p[j + 1] == '*':
                    memory[i][j] = memory[i][j + 2]
                    if match:
                        memory[i][j] = memory[i + 1][j] or memory[i][j]
                elif match:
                    memory[i][j] = memory[i + 1][j + 1]

        return memory[0][0]





sol = Solution()
res1 = sol.isMatch("aa", "a")
res2 = sol.isMatch("aa", "a*")
res3 = sol.isMatch("ab", ".*")
print(res1, res2, res3)
