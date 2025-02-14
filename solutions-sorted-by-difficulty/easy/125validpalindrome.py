class Solution:
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]

solution = Solution()
print(solution.isPalindrome("1b1"))
