class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
         return int(bin(n)[2:].zfill(32)[::-1], 2)



sol = Solution()
res = sol.reverseBits(10100101000001111010011100)
print(res)

