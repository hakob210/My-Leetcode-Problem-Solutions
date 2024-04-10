class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort(reverse=True)
        n = len(deck)
        dq = [deck[0]]

        for i in range(1, n):
            x = dq.pop()
            dq.insert(0, x)
            dq.insert(0, deck[i])

        return dq




sol = Solution()
res = sol.deckRevealedIncreasing([17,13,11,2,3,5,7])
print(res)
