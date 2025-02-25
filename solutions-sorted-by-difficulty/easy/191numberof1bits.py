class Solution(object):
    def hammingWeight(self, n):
        count=0
        while n>0:
            if(n & 1):
                count+=1
            n>>=1
        return count

solution = Solution()
print(solution.hammingWeight(1))