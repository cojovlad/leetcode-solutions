class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                if count > max:
                    max = count
                count = 0
        if count > max:
            max = count
        return max

solution = Solution()
print(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
