class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0

        for last in s[::-1]:
            if last == " ":
                s = s[:-1]
            else:
                break

        for i in s[::-1]:
            if i != " ":
                length += 1
            else:
                break

        return length






sol = Solution()
res = sol.lengthOfLastWord("fbiuwrb euigfglwieufvlw wfuvbwkurfyfvbwkeury bwkeuyfybwkeu    ")
print(res)
