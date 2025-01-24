class Solution(object):
    def removeDuplicates(self, nums):
        hashmap = {}

        for num in nums:
            hashmap[num] = True

        nums[:] = sorted(hashmap.keys())

        return len(nums)


    @staticmethod
    def run():
        nums = [1, 1, 2, -1, -1]
        solution = Solution()
        result = solution.removeDuplicates(nums)
        print(f"Number of unique elements: {result}")
        print(f"Number of unique elements: {nums}")

Solution.run()