class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        maxCount = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 1
        return max(maxCount, count)

solution = Solution()
print(solution.findLengthOfLCIS([1,3,5,4,7]))