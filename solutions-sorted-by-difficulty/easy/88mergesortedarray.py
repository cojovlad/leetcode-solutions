class Solution(object):
    def merge(self, nums1, m, nums2, n):
        copyOfNums1 = nums1[:m]
        nums1.clear()
        i = 0
        j = 0

        while i < m and j < n:
            if copyOfNums1[i] < nums2[j]:
                nums1.append(copyOfNums1[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1

        while i < m:
            nums1.append(copyOfNums1[i])
            i += 1

        while j < n:
            nums1.append(nums2[j])
            j += 1

        return nums1

solution = Solution()
print(solution.merge([1, 2, 3], 3, [2, 3, 4], 3))
