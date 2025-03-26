class Solution:
    def thirdMax(self, nums):
        nums = list(set(nums))  # Remove duplicates
        first, second, third = float('-inf'), float('-inf'), float('-inf')

        for num in nums:
            if num > first:
                third, second, first = second, first, num
            elif num > second:
                third, second = second, num
            elif num > third:
                third = num

        return third if third != float('-inf') else first


solution = Solution()
print(solution.thirdMax([1, 2, -2147483648]))  # Output: -2147483648
