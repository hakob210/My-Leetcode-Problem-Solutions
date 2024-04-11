class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        numStack = []

        for digit in num:
            while k > 0 and numStack and digit < numStack[-1]:
                numStack.pop()
                k -= 1
            numStack.append(digit)

        while k > 0 and numStack:
            numStack.pop()
            k -= 1

        temp = ""
        while numStack:
            temp += numStack.pop()
        temp = temp[::-1]

        result = ""
        foundNonZero = 0
        for digit in temp:
            if digit == '0' and foundNonZero == 0:
                continue
            else:
                result += digit
                foundNonZero = 1
        if not result:
            result = '0'
        return result







sol = Solution()
res1 = sol.removeKdigits("1432219", 3)
res2 = sol.removeKdigits("10200", 1)
res3 = sol.removeKdigits("10", 2)
print(res1, res2, res3)
