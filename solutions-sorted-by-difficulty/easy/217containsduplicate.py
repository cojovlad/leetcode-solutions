class Solution(object):
    def containsDuplicate(self, nums):
        appeared={}
        for num in nums:
            if num in appeared:
                return True
            appeared[num]=1
        return False


solution = Solution()
print(solution.containsDuplicate([1, 2, 7, 7]))
