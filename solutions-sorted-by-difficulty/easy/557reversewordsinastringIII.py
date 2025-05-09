class Solution(object):
    def reverseWords(self, s):
        emptyString=""
        for word in s.split():
            emptyString=emptyString+word[::-1]
            emptyString+=" "
        return emptyString[:-1]
solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))