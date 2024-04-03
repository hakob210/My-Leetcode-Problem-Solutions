class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dic={}
        dic2={}
        s=s.split(' ')
        if len(s)!=len(pattern):
            return(False)
        for i,j in zip(pattern,s):
            if i in dic:
                if dic[i]!=j:
                    return(False)
            else:
                dic[i]=j
            if j in dic2:
                if dic2[j]!=i:
                    return(False)
            else:
                dic2[j]=i
        return(True)
        








sol = Solution()
res = sol.wordPattern("abba", "dog cat cat dog")
print(res)
