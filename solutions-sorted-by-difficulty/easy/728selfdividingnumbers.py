class Solution(object):
    def selfDividingNumbers(self, left, right):
        newList=[]
        for i in range(left, right + 1):
            num = i
            ok = 1
            while num != 0:
                digit = num % 10
                if digit == 0 or i % digit != 0:
                    ok = 0
                    break
                num //= 10
            if ok == 1:
                newList.append(i)
        return newList

solution = Solution()
print(solution.selfDividingNumbers(1, 22))
