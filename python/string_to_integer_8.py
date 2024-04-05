class Solution(object):
    def myAtoi(self, s):
        r = ''
        ints = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+'])

        s = s.lstrip()

        sign_allowed = True
        for i, char in enumerate(s):
            if char in ints:
                if char == '-' or char == '+':
                    if sign_allowed:
                        r += char
                        sign_allowed = False
                    else:
                        break
                else:
                    r += char
                    sign_allowed = False
            else:
                break

        if not r or r == '-' or r == '+':
            return 0

        try:
            num = int(r)
            if num < -2**31:
                return -2**31
            elif num > 2**31-1:
                return 2**31-1
            else:
                return num
        except ValueError:
            return 0













sol = Solution()
res = sol.myAtoi("       +-12 aaaa")
print(res)

