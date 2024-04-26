from collections import deque

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        counts = [0] * n
        links = [0] * n
        
        for edge in edges:
            links[edge[0]] ^= edge[1]
            counts[edge[0]] += 1
            links[edge[1]] ^= edge[0]
            counts[edge[1]] += 1
        
        Qu = deque()
        dists = [0] * n
        
        for i in range(n):
            if counts[i] == 1:
                Qu.append(i)
        
        stp = 1
        while Qu:
            size = len(Qu)
            for _ in range(size):
                tmp = Qu.popleft()
                links[links[tmp]] ^= tmp
                counts[links[tmp]] -= 1
                if counts[links[tmp]] == 1:
                    dists[links[tmp]] = max(stp, dists[links[tmp]])
                    Qu.append(links[tmp])
            stp += 1
        
        max_dist = max(dists)
        res = [i for i in range(n) if dists[i] == max_dist]
        
        return res





sol = Solution()
res = sol.findMinHeightTrees(4, [[1,0],[1,2],[1,3]])
print(res)
