class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x

        last_guess = x / 2.0
        while True:
            guess = (last_guess + x / last_guess) / 2
            if abs(guess - last_guess) < 0.000001:
                return int(guess)
            last_guess = guess

solution = Solution()
print(solution.mySqrt(26))
