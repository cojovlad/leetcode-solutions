class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_number=max(freq,key=freq.get)
        return max_number

solution = Solution()
print(solution.majorityElement([1,1,2,3,3,4,4]))
