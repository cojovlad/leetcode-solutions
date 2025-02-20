class Solution(object):
    def titleToNumber(self, columnTitle):
        result = 0
        for character in columnTitle:
            result = result * 26 + ord(character) - ord('A') + 1
        return result

solution = Solution()
print(solution.titleToNumber("A"))  # Output: 28
