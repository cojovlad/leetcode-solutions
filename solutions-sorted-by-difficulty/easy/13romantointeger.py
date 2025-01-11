class Solution(object):
    def romanToInt(self, s):
        romanToInt = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        previousValue = 0

        for char in reversed(s):
            currentValue = romanToInt[char]
            if currentValue < previousValue:
                total -= currentValue
            else:
                 total += currentValue
            previousValue = currentValue

        return total

    @staticmethod
    def run():
        roman = (input("Enter the target: "))
        solution = Solution()
        result = solution.romanToInt(roman)
        print(result)
Solution.run()
