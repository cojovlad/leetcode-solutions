class Solution(object):
    def intersect(self, nums1, nums2):
        newList=[]
        hashTable1={}
        hashTable2={}
        for num in nums1:
            hashTable1[num] = hashTable1.get(num, 0) + 1
        for num in nums2:
            hashTable2[num] = hashTable2.get(num, 0) + 1
        for num in hashTable1:
            if num in hashTable2:
                min_count = min(hashTable1[num], hashTable2[num])
                newList.extend([num]*min_count)
        return newList

solution = Solution()
print(solution.intersect([1,2,2,1],[2,2]))