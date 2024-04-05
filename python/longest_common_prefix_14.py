class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        min_length = min(len(s) for s in strs)
        
        for i in range(min_length):

            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:

                    return strs[0][:i]
        
        return strs[0][:min_length]





sol = Solution()
res = sol.longestCommonPrefix(["godzilla", "gorilla"])
print(res)
