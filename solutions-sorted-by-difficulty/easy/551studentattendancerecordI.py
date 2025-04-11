class Solution(object):
    def checkRecord(self, s):
        L=0
        longestL=0
        A=0
        for attendance in s:
            if attendance=='L':
                L+=1
            else:
                if L>longestL:
                    longestL=L
                if attendance=='A':
                    A+=1
                L = 0
        if L>longestL:
            longestL=L
        return False if A>1 or longestL>2 else True

solution = Solution()
print(solution.checkRecord("LPLPLPLPLPL"))
