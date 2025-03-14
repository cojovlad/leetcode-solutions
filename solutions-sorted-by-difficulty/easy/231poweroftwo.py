class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        if n == 2:
            return True
        number=2
        while number <= n:
            number *= 2
            if number == n:
                return True
        return False

solution = Solution()
print(solution.isPowerOfTwo(15))