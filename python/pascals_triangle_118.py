class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1], [1,1]]

        if numRows == 0:

            return []

        elif numRows == 1:

            return [[1]]

        else:

            for i in range(1, numRows-1):
                row = [1]
                for j in range(0, len(triangle[i])-1):
                    row.append(triangle[i][j] + triangle[i][j+1])

                row.append(1)
                triangle.append(row)

            return triangle



sol = Solution()
res = sol.generate(7)
print(res)

