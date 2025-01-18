class Solution(object):
    def isValid(self, s):
        openParanthesesStack = []
        mapOfClosingBrackets = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in mapOfClosingBrackets.values():
                openParanthesesStack.append(char)
            elif char in mapOfClosingBrackets.keys():
                if not openParanthesesStack or openParanthesesStack[-1] != mapOfClosingBrackets[char]:
                    return False
                openParanthesesStack.pop()
            else:
                return False
        return not openParanthesesStack

    @staticmethod
    def run():
        s = "( { [ ] } )"
        solution = Solution()
        result = solution.isValid(s)
        print(f"Is the string '{s}' valid? {result}")


# Run the program
Solution.run()
