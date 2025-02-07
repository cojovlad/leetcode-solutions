class Solution(object):
    def addBinary(self, a, b):
        num1, num2 = 0, 0

        for char in a:
            num1 = num1 * 2 + int(char)

        for char in b:
            num2 = num2 * 2 + int(char)

        total = num1 + num2

        binary_result = ''
        if total == 0:
            binary_result = '0'
        else:
            while total > 0:
                binary_result = str(total % 2) + binary_result
                total //= 2

        return binary_result

    @staticmethod
    def run():
        a = "11"
        b = "1"
        sol = Solution()
        result = sol.addBinary(a, b)
        print("Binary sum:", result)

Solution.run()
