class Solution(object):
    def findLUSlength(self, a, b):
        if a == b:
            return -1
        return max(len(a), len(b))
solution = Solution()
print(solution.findLUSlength("aaa","bbb"))