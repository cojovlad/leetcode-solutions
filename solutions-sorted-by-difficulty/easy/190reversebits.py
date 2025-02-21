class Solution:
    def reverseBits(self, n):
        result=0
        for i in range(32):
            result = (result<<1) | (n&1)
            n>>=1
        return result


solution = Solution()
print(solution.reverseBits(0o0000010100101000001111010011100))
