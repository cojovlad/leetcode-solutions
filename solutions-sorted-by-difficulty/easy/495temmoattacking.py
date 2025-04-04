class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        totalDuration = 0
        for i in range(len(timeSeries) - 1):
            totalDuration += min(duration,timeSeries[i+1]-timeSeries[i])
        return totalDuration + duration

solution = Solution()
print(solution.findPoisonedDuration([1, 2,3,4,5], 5))
