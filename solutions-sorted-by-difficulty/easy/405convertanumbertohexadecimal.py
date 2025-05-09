class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        result = ""

        if num < 0:
            num += 2 ** 32

        while num > 0:
            digit = num % 16
            result = hex_chars[digit] + result
            num //= 16

        return result

solution = Solution()
print(solution.toHex(26))
