class Solution(object):
    def countBits(self, n):
        list=[]
        for i in range(n+1):
            binaryString = bin(i)[2::]
            list.append(binaryString.count('1'))
        return list

solution = Solution()
print(solution.countBits(5))
