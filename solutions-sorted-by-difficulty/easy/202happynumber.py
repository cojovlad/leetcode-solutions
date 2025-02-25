class Solution(object):
    def isHappy(self, n):

        seen_numbers={}
        while(n!=1):
            if n in seen_numbers:
                return False

            seen_numbers[n] = True

            sumOfSquares=0
            while n:
                digit = n % 10
                sumOfSquares += digit * digit
                n //= 10

            n=sumOfSquares
        return True


solution = Solution()
print(solution.isHappy(20))