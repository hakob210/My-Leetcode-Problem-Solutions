class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        newList = []

        for row in range(0, len(matrix)):
            newRow = []
            for column in range(0, len(matrix[row])):
                newRow.append(matrix[column][row])
            newList.append(newRow)

        for row in range(0, len(newList)):
            matrix[row] = newList[row][::-1]

        return matrix





sol = Solution()
res = sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
print(res)
                
