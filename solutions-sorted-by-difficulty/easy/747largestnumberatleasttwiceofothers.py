class Solution(object):
    def dominantIndex(self, nums):
        max=0
        secondMax=0
        position=0
        for i,num in enumerate(nums):
            if num > max:
                secondMax=max
                max=num
                position=i
            elif num > secondMax:
                secondMax=num
        return position if max >= secondMax * 2 else -1
solution = Solution()
print(solution.dominantIndex([0,0,3,2]))