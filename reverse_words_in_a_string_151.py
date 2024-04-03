class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []
        word = ""
        sentence = ""

        for i in s:
            if i != " ":
                word += i
            elif word:
                l.append(word)
                word = ""

        if word:
            l.append(word)

        for j in l[::-1]:
            sentence += j + " "

        return sentence.strip()










sol = Solution()
res1 = sol.reverseWords("rythm. no got have feet guilty again, dance gonna never I'm")
res2 = sol.reverseWords("              lalala   aaaa  ")
print(res1, res2)
