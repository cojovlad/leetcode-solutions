class Solution(object):
    def intersection(self, nums1, nums2):
        intersectionArray=[]
        for num in nums1:
            if num in nums2:
                if(num not in intersectionArray):
                    intersectionArray.append(num)
        return intersectionArray

solution = Solution()
print(solution.intersection([1,2,2,1],[2,2]))
