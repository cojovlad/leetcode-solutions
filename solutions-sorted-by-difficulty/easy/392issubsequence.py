class Solution(object):
    def isSubsequence(self, s, t):
        i=0
        j=0
        if s == "":
            return True
        if t == "":
            return False

        while(i < len(s)) and j < len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1
            if(i < len(s) and j == len(t)):
                return False
        return True

solution = Solution()
print(solution.isSubsequence("abc","ahbgdc"))