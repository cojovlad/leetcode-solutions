class Solution(object):
    def isPerfectSquare(self, num):
        left, right = 1, num

        while left <= right:
            mid = left + (right - left) // 2
            square=mid*mid
            if mid ** 2 == num:
                return True
            elif square<num:
                left=mid+1
            else:
                right=mid-1
        return False

solution = Solution()
print(solution.isPerfectSquare(16))