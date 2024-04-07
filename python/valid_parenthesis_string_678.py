class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack_open = []
        stack_star = []

        for i, char in enumerate(s):
            if char == "(":
                stack_open.append(i)
            elif char == "*":
                stack_star.append(i)
            elif char == ")":
                if stack_open:
                    stack_open.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False

        while stack_open and stack_star:
            if stack_open[-1] < stack_star[-1]:
                stack_open.pop()
                stack_star.pop()
            else:
                return False

        return len(stack_open) == 0










sol = Solution()
res = sol.checkValidString("()")
print(res)
