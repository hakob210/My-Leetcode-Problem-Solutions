class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        r = 0
        i = 0
        
        while i < len(nums):
            if nums[i] != val:
                r += 1
                i += 1
            else:
                nums.pop(i)
                
        return r






sol = Solution()
res = sol.removeElement([0,1,2,2,3,0,4,2], 2)
print(res)


