class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        return max(
            nums[-1] * nums[-2] * nums[-3],
            nums[0] * nums[1] * nums[-1]
        )

solution = Solution()
print(solution.maximumProduct([1,2,3]))