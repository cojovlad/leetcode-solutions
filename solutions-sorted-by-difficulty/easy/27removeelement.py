class Solution(object):
    def removeElement(self, nums, val):
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
            else:
                nums[i] = None
        return count

    @staticmethod
    def run():
        nums = [3, 2, 2, 3]
        val = 3
        sol = Solution()
        k = sol.removeElement(nums, val)
        print("New length:", k)
        print("Modified nums:", nums[:k])

Solution.run()
