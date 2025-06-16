class Solution(object):
    def twoSum(self, nums, target):
        hashMap={}
        for i,num in enumerate(nums):
            diff=target - num
            if diff in hashMap:
                return [hashMap[diff],i]
            hashMap[num]=i
        return []
