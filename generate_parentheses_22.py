class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(cur, left_p, right_p):
            if len(cur) == 2 * n:
                self.res.add(cur)
                return
            if left_p < n:
                helper(cur + '(', left_p + 1, right_p)
            if right_p < left_p:
                helper(cur + ')', left_p, right_p + 1)

        self.res = set()
        helper('', 0, 0)
        return list(self.res)





sol = Solution()
res = sol.generateParenthesis(3)
print(res)

