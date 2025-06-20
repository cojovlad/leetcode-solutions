class Solution(object):
    def longestConsecutive(self, nums):
        listOfNums=set(nums)
        longestSection=0
        for num in listOfNums:
            numberCheck=num-1
            if numberCheck not in listOfNums:
                section=1
                while num+1 in listOfNums:
                    section+=1
                    num+=1
                if(section>longestSection):
                    longestSection=section
        return longestSection

solution = Solution()
print(solution.longestConsecutive([0,3,7,2,5,8,4,0,1]))

#O(n+max)
# def longestConsecutive(self, nums):
#     numberList = {}
#     max = 0
#
#     for num in nums:
#         numberList[num] = 1
#         if (max < num):
#             max = num
#     sectionCount = 0
#     maxSection = 0
#     for i in range(max + 1):
#         if (i in numberList):
#             if (sectionCount == 0):
#                 sectionCount = 1
#             else:
#                 sectionCount += 1
#         else:
#             if (sectionCount > maxSection):
#                 maxSection = sectionCount
#                 sectionCount = 0
#     if (sectionCount > maxSection):
#         maxSection = sectionCount
#     return maxSection