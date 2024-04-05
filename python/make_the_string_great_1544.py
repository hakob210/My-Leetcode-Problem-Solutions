class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = [] 

        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)








sol = Solution()
res1 = sol.makeGood("leEeetcode")
res2 = sol.makeGood("abBAcC")
print(res1, res2)
