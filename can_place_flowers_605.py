class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        def is_last_index(lst, index):
            return index == len(lst) - 1

        l = 0

        if flowerbed == [0, 0]:
            return n <= 1

        for i in range(0, len(flowerbed) - 1):
            if flowerbed[i] == 1 and i != len(flowerbed) - 1:
                flowerbed[i+1] = 2
            elif flowerbed[i] == 0 and flowerbed[i+1] != 1 and i != len(flowerbed) - 2:
                flowerbed[i+1] = 2

        reverse = flowerbed[::-1]

        for j in range(0, len(flowerbed) - 1):
            if reverse[j] == 1 and j != len(reverse) - 1:
                reverse[j+1] = 2
            elif reverse[j] == 0 and reverse[j+1] != 1 and j != len(reverse) - 2:
                reverse[j+1] = 2

        flowerbed = reverse[::-1]

        for f in flowerbed:
            if f == 0:
                l += 1
        print(flowerbed)
        return l >= n





sol = Solution()
res = sol.canPlaceFlowers([0, 0], 2)
print(res)
