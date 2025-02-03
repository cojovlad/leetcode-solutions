class Solution(object):
    def plusOne(self, digits):
        num = 0
        for digit in digits:
            num = num * 10 + digit
        num += 1
        return [int(d) for d in str(num)]

    @staticmethod
    def run():
        digits = [9]
        sol = Solution()
        result = sol.plusOne(digits)
        print("Resulting array:", result)

Solution.run()