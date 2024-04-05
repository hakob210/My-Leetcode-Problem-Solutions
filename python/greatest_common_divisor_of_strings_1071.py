class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        gcd_length = gcd(len(str1), len(str2))
        gcd_str = str1[:gcd_length]

        if str1.replace(gcd_str, '') == '' and str2.replace(gcd_str, '') == '':
            return gcd_str
        else:
            return ""






sol = Solution()
res = sol.gcdOfStrings("e89ie89ie89ie89ie89ie89ie89ie89i", "e89ie89i")
print(res)
