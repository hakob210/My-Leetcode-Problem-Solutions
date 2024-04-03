class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        max_length = 0
        start = 0
        char_index = {}
        
        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            else:
                max_length = max(max_length, i - start + 1)
            char_index[char] = i
        
        return max_length







sol = Solution()
res = sol.lengthOfLongestSubstring("abciabcabcdefhuxzsqwebbccbbdd")
print(res)
