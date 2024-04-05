class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        numbers = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def generate_combinations(index, path):
            if index == len(digits):
                combinations.append(path)
                return
            letters = numbers[int(digits[index])]
            for letter in letters:
                generate_combinations(index + 1, path + letter)

        combinations = []
        generate_combinations(0, '')
        return combinations
        









sol = Solution()
res = sol.letterCombinations("23")
print(res)
