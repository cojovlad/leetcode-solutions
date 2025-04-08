class Solution(object):
    def fib(self, n):
        if n==0 or n==1:
            return n
        a,b=0,1
        for i in range(n-1):
            a,b=b,a+b
        return b

solution = Solution()
print(solution.fib(4))