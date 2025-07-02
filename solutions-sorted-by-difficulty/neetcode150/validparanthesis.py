class Solution:
    def isValid(self, s):
        stack = []
        if len(s) == 1:
            return False
        for element in s:
            if element == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif element == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif element == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif element in "({[":
                stack.append(element)
            else:
                stack.append(element)
        return len(stack) == 0

solution = Solution()
print(solution.isValid("]]"))
