class Solution(object):
    def guessNumber(self, n):
        l, r = 1, n

        while l <= r:
            mid = l + (r - l) // 2
            result = guess(mid) #has error because problem contains an additional method

            if result == 0:
                return mid
            elif result == -1:
                r = mid - 1
            else:
                l = mid + 1

solution = Solution()
print(solution.guessNumber(16))