class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        current_count = 0
        
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        
        res = max(res, current_count)
        
        for i in range(k, len(s)):
            if s[i] in vowels:
                current_count += 1
            if s[i - k] in vowels:
                current_count -= 1
            res = max(res, current_count)
        
        return res






sol = Solution()
res1 = sol.maxVowels("abciiidef", 3)
res2 = sol.maxVowels("aeiou", 2)
res3 = sol.maxVowels("leetcode", 3)
print(res1, res2)
