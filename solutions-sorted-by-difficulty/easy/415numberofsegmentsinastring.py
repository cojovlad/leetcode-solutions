class Solution(object):
    def countSegments(self, s):
        words=s.split()
        return len(words)

solution = Solution()
print(solution.countSegments("121 1"))