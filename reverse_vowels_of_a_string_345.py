class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"])
        v = []
        l = []
        ans = ""

        for i in s:
            if i in vowels:
                v.append(i)
                l.append("_")
            else:
                l.append(i)

        reverse = v[::-1]

        for j in l:
            if j == "_":
                ans += reverse[0]
                reverse.pop(0)
            else:
                ans += j

        return ans


        

    







sol = Solution()
res = sol.reverseVowels("leetcode")
print(res)
