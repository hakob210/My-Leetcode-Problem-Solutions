class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if n == 1:
            return True
        visited = [False] * n
        visited[source] = True
        flag = True
        while flag:
            flag = False
            for edge in edges:
                if visited[edge[0]] != visited[edge[1]]:
                    visited[edge[0]] = True
                    visited[edge[1]] = True
                    flag = True
                if visited[destination]:
                    return True
        return False





sol = Solution()
res1 = sol.validPath(3, [[0,1],[1,2],[2,0]], 0, 2)
res2 = sol.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)
print(res1, res2)
