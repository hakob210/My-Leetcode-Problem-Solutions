class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r = 0

        answer = []

        for i in range(n):
            r += 1
            if r % 3 == 0 and r % 5 == 0:
                answer.append("FizzBuzz")
            elif r % 3 == 0 and r % 5 != 0:
                answer.append("Fizz")
            elif r % 5 == 0 and r % 3 != 0:
                answer.append("Buzz")
            else:
                answer.append(str(r))

        return answer







sol = Solution()
res = sol.fizzBuzz(17)
print(res)
