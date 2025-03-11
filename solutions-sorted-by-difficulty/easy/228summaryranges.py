class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []

        resultList = []
        currentList = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                currentList.append(nums[i])
            else:
                resultList.append(f"{currentList[0]}" if len(currentList) == 1 else f"{currentList[0]}->{currentList[-1]}")
                currentList = [nums[i]]

        resultList.append(f"{currentList[0]}" if len(currentList) == 1 else f"{currentList[0]}->{currentList[-1]}")
        return resultList

solution = Solution()
print(solution.summaryRanges([0,2,3,4,6,8,9]))
