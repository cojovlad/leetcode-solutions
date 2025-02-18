class Solution(object):
    def convertToTitle(self, columnNumber):
        result=[]
        while(columnNumber>0):
            columnNumber-=1
            num=columnNumber%26
            result.append(chr(num+ord('A')))
            columnNumber//=26
        return ''.join(result[::-1])
solution = Solution()
print(solution.convertToTitle(701));
