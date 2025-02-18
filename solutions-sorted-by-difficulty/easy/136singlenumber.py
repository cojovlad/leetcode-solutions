class Solution(object):
    def singleNumber(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num,count in freq.items():
            if count == 1:
                return num


solution = Solution()
print(solution.singleNumber([1,1,2,3,3,4,4]))
