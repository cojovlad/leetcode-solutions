class Solution(object):
    def twoSum(self, nums, target):
        hasmap={}
        for i,num in enumerate(nums):

            diff=target - num
            if diff in hasmap:
                print(hasmap)
                return [hasmap[diff],i]
            else:
                hasmap[num]=i
        return []

    @staticmethod
    def run():
        nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
        target = int(input("Enter the target: "))
        solution = Solution()
        result = solution.twoSum(nums, target)
        print("Indices:", result)

Solution.run()
