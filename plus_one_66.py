class Solution(object):
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            if digits[i] < 10:
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits




sol = Solution()
res = sol.plusOne([9, 9, 9, 9])
print(res)
