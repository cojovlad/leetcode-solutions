class Solution(object):
    def maxCount(self, m, n, ops):
        if not ops:
            return n*m
        minA=min(op[0] for op in ops)
        minB=min(op[1] for op in ops)
        return minA * minB

solution = Solution()
print(solution.maxCount(3,3,[[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]))

