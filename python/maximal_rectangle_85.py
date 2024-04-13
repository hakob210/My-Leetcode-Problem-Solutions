class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        r, c=len(matrix), len(matrix[0])
        if r==1 and c==1:
            if matrix[0][0]=='1': return 1
            else: return 0
        h=[0]*(c+1)
        maxArea=0

        for i, row  in enumerate(matrix):
            st=[-1] 
            row.append('0')
            for j, x in enumerate(row):
                if x=='1': h[j]+=1
                else: h[j]=0
                while len(st)>1 and (j==c or h[j]<h[st[-1]]):
                    m=st[-1]
                    st.pop()
                    w=j-st[-1]-1
                    area=h[m]*w
                    maxArea=max(maxArea, area)
                st.append(j)
        return maxArea

        



sol = Solution()
res1 = sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
res2 = sol.maximalRectangle([["0"]])
res3 = sol.maximalRectangle([["1"]])
print(res1, res2, res3)
