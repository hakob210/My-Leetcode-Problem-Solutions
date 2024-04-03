class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        curr = 0
        prev = 0

        for i in s[::-1]:
            number = roman[i]
            if number < prev:
                curr -= number
            else:
                curr += number
            prev = number

        return curr

       







sol = Solution()
res = sol.romanToInt("MCLXVIII")
print(res)
