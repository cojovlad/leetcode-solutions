class Solution(object):
    def findComplement(self, num):
        bitLength=num.bit_length()
        mask=(1<<bitLength)-1
        print(mask)
        return num^mask

solution = Solution()
print(solution.findComplement(5))