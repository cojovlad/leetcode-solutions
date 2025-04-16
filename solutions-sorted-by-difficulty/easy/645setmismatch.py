class Solution(object):
    def findErrorNums(self, nums):
        duplicate = -1
        missing = -1
        numSet = set()
        for num in nums:
            if num not in numSet:
                numSet.add(num)
            else:
                duplicate = num
        for i in range(1,len(nums)+1):
            if i not in numSet:
                missing = i
                break
        return [duplicate, missing]

solution = Solution()
print(solution.findErrorNums([2, 2, 3]))
