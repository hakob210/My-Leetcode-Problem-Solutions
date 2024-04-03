class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        copy = nums
        for i in copy:
            if nums.count(i) > 1:
                while nums.count(i) > 1:
                    nums.remove(i)
                

        return len(nums)




sol = Solution()
res = sol.removeDuplicates([1, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7])
print(res)
