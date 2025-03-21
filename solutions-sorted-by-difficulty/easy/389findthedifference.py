class Solution(object):
    def findTheDifference(self, s, t):
        xorResult=0
        for char in s:
            xorResult=xorResult^ord(char)
        for char in t:
            xorResult=xorResult^ord(char)
        return chr(xorResult)

solution = Solution()
print(solution.findTheDifference("abcd","abcde"))