class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        remove_indices = set()
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    remove_indices.add(i)
        
        remove_indices.update(stack)
        
        result = ''.join(char for i, char in enumerate(s) if i not in remove_indices)
        
        return result






sol = Solution()
res = sol.minRemoveToMakeValid("lee(t(c)o)de)")
print(res)
