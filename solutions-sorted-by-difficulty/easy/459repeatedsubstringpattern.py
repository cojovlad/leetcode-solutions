class Solution(object):
    def repeatedSubstringPattern(self, s):
        # solution 1
        n = len(s)
        sCopy = s
        i = 0
        while n > 1:
            sCopy = sCopy[1:] + s[i]
            n -= 1
            i += 1
            if (s == sCopy):
                return True
        return False

    # solution 2
    # return s in (s + s)[1:-1]


solution = Solution()
print(solution.repeatedSubstringPattern("abcabc"))
