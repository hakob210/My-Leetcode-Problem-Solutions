class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 0:
            return 0
        
        count = 1
        prev_char = chars[0]
        write_index = 0
        
        for i in range(1, len(chars)):
            if chars[i] == prev_char:
                count += 1
            else:
                chars[write_index] = prev_char
                write_index += 1
                if count > 1:
                    for digit in str(count):
                        chars[write_index] = digit
                        write_index += 1
                prev_char = chars[i]
                count = 1
        
        chars[write_index] = prev_char
        write_index += 1
        if count > 1:
            for digit in str(count):
                chars[write_index] = digit
                write_index += 1
        
        return write_index











sol = Solution()
res = sol.compress(["a","a","b","b","c","c","c"])
print(res)
