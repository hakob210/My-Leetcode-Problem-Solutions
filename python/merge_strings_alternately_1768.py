class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        r = ""
        min_len = min(len(word1), len(word2))
        
        for i in range(min_len):
            r += word1[i]
            r += word2[i]
        
        r += word1[min_len:] + word2[min_len:]
        
        return r






sol = Solution()
res = sol.mergeAlternately("abc", "pqr")
print(res)
