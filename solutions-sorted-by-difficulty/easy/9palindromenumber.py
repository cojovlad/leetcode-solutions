class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        if x < 10:
            return True

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10

    @staticmethod
    def run():
        palindrome = int(input("Enter the target: "))
        solution = Solution()
        result = solution.isPalindrome(palindrome)
        print(result)
Solution.run()
