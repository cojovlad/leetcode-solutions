class Solution(object):
    def findDisappearedNumbers(self, nums):
        mapOfNumbers=set()
        dissapeared=[]
        for num in nums:
            mapOfNumbers.add(num)

        for i in range(1,len(nums)+1):
            if i not in mapOfNumbers:
                dissapeared.append(i)
        return dissapeared

solution = Solution()
print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))