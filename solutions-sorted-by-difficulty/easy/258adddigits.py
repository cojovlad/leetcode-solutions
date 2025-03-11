class Solution(object):
    def addDigits(self, num):
        while num > 9:
            numCopy=num
            newNumber=0
            while numCopy:
                newNumber +=numCopy%10
                numCopy = numCopy//10
            num = newNumber
        return int(num)

solution = Solution()
print(solution.addDigits(38))