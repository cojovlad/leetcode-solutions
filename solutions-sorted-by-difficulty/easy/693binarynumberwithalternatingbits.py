class Solution(object):
    def hasAlternatingBits(self, n):
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0

solution = Solution()
print(solution.hasAlternatingBits(5))
