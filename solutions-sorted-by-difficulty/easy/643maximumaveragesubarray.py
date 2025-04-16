class Solution(object):
    def findMaxAverage(self, nums, k):

        windowSum=sum(nums[:k])
        maxSum=windowSum
        for i in range(k,len(nums)):
            windowSum += nums[i] - nums[i-k]
            maxSum = max(maxSum,windowSum)
        return float(maxSum)/k

solution = Solution()
print(solution.findMaxAverage([1,12,-5,-6,50,3],4))
