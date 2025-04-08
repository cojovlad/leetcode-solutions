class Solution(object):
    def checkPerfectNumber(self, num):
        if num <=1:
            return False
        sum = 1
        for integer in xrange(2, num):
            if(integer * integer > num):
                break
            if(num % integer == 0):
                sum+=integer
                if(num//integer != integer):
                    sum+=num//integer
        return sum == num

solution = Solution()
print(solution.checkPerfectNumber(28))
