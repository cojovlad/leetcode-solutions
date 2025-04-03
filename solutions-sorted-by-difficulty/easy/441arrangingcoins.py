class Solution(object):
    def arrangeCoins(self, n):
        i=1
        result=1
        ok=1
        while(ok==1):
            if n-i>0 or n-i==0:
                ok=1
                result=i
            else:
                ok=0
            n-=i
            i+=1
        return result



solution = Solution()
print(solution.arrangeCoins(8))