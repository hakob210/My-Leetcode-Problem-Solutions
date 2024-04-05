class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        r = ""

        if numRows == 1 or numRows >= len(s):
            return s
    
        rows = [''] * numRows
    
        current_row = 0
    
        for char in s:
            rows[current_row] += char
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1
            current_row += direction
    
        for row in rows:
            r += row

        return r













sol = Solution()
res = sol.convert("PAYPALISHIRING", 4)
print(res)
