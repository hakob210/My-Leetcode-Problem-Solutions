class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)

        for i in range(0, l):
            nums.append(nums[i])

        return nums





sol = Solution()
res = sol.getConcatenation([1, 2, 3, 4, 5])
print(res)
