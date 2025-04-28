class Solution(object):
    def search(self, nums, target):
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return -1

solution = Solution()
print(solution.search([1,2,3,4,5,6,7,8,9],5))