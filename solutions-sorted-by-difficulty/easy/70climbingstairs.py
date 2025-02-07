class Solution(object):
    def climbStairs(self, n):
        first,second = 1, 1
        sum=0
        if n == 1:
            return 1
        while(n>1):
            sum=first+second
            first=second
            second=sum
            n-=1
        return sum

solution = Solution()
print(solution.climbStairs(7))