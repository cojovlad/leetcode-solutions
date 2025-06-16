class Solution(object):
    def containsDuplicate(self, nums):
        numsCheck=set()
        for num in nums:
            if num in numsCheck:
                return True
            numsCheck.add(num)
        return False
