class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        mapping={}
        for i, num in enumerate(nums):
            if num in mapping and i-mapping[num] <= k:
                return True
            mapping[num]=i
        return False

solution = Solution()
print(solution.containsNearbyDuplicate([1, 2, 7, 7],6))