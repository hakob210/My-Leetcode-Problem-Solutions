class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        ans = [1] * n

        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]

        for i in range(n):
            ans[i] = left_products[i] * right_products[i]

        return ans











sol = Solution()
res = sol.productExceptSelf([1, 2, 3, 4, 5, 6, 7])
print(res)
