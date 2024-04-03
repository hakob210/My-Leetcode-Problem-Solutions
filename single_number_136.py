class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result




sol = Solution()
res = sol.singleNumber([3, 3, 5, 5, 7])
print(res)
