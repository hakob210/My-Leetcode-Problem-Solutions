class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        else:
            map_chars = {}
            set_vals = set()
            for i in range(len(s)):
                if s[i] in map_chars:
                    if map_chars[s[i]] != t[i]:
                        return False
                else:
                    if t[i] in set_vals:
                        return False
                    map_chars[s[i]] = t[i]
                    set_vals.add(t[i])
            return True











sol = Solution()
res = sol.isIsomorphic("egg", "add")
print(res)
