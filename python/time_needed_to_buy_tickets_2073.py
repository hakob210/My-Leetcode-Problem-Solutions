class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        r = 0
        for i, x in enumerate(tickets):
            if i <= k:
                r += min(tickets[i], tickets[k])
            else:
                r += min(tickets[i], tickets[k] - 1)

        return r



sol = Solution()
res1 = sol.timeRequiredToBuy([2,3,2], 2)
res2 = sol.timeRequiredToBuy([5,1,1,1], 0)
res3 = sol.timeRequiredToBuy([84,49,5,24,70,77,87,8], 3)
print(res1, res2, res3)
