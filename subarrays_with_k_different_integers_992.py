class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        count1 = [0] * (len(nums) + 1)
        count2 = [0] * (len(nums) + 1)
        
        unique1 = 0
        unique2 = 0
        l1 = 0
        l2 = 0
        
        for r in range(len(nums)):
            if count1[nums[r]] == 0:
                unique1 += 1
            count1[nums[r]] += 1
            
            if count2[nums[r]] == 0:
                unique2 += 1
            count2[nums[r]] += 1
            
            while unique1 > k:
                count1[nums[l1]] -= 1
                if count1[nums[l1]] == 0:
                    unique1 -= 1
                l1 += 1
                
            while unique2 >= k:
                count2[nums[l2]] -= 1
                if count2[nums[l2]] == 0:
                    unique2 -= 1
                l2 += 1
                
            ans += l2 - l1
            
        return ans







sol = Solution()
res = sol.subarraysWithKDistinct([1, 2, 1, 2, 3], 2)
print(res)

