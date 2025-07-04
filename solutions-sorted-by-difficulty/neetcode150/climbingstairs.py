class Solution(object):
    def climbStairs(self, n):
        a, b = 1, 1
        for i in range(1,n):
            a, b = b, a + b
        return b



solution = Solution()
print(solution.climbStairs(6))