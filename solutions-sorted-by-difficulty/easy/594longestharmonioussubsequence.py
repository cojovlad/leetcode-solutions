class Solution(object):
    def findLHS(self, nums):

        mapOfNumber={}
        for num in nums:
            mapOfNumber[num] = mapOfNumber.get(num, 0) + 1
        maxHarmony=0
        for num in nums:
            if num + 1 in mapOfNumber:
                currentLength = mapOfNumber[num + 1] + mapOfNumber[num]
                if currentLength > maxHarmony:
                    maxHarmony = currentLength
        return maxHarmony

solution = Solution()
print(solution.findLHS([1,3,2,2,5,2,3,7]))