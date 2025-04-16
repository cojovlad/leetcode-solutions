class Solution(object):
    def calPoints(self, operations):
        stack=[]
        for operation in operations:
            if operation == 'C':
                stack.pop()
            elif operation == '+':
                stack.append(stack[-1]+stack[-2])
            elif operation == 'D':
                stack.append(stack[-1]*2)
            else:
                stack.append(int(operation))
        return sum(stack)

solution = Solution()
print(solution.calPoints(["5","2","C","D","+"]))