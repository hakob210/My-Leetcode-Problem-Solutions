class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0
        d = [0]

        for i in s:
            if i == "(":
                depth += 1
            elif i == ")":
                d.append(depth)
                depth -= 1

        return max(d)
        











sol = Solution()
res = sol.maxDepth("(1+(2*3)+((8)/4))+1")
print(res)
