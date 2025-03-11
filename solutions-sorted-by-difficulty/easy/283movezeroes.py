class Solution(object):
    def moveZeroes(self, nums):
        newArray=[]
        for i in range(len(nums)):
            if nums[i] != 0:
                newArray.append(nums[i])
        for i in range(len(nums)):
            if nums[i] == 0:
                newArray.append(nums[i])
        for i in range(len(newArray)):
            nums[i] = newArray[i]

solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))