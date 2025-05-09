class Solution(object):
    def transpose(self, matrix):
        R, C = len(matrix), len(matrix[0])
        newMatrix = [[0] * R for _ in range(C)]
        for i in range(R):
            for j in range(C):
                newMatrix[j][i]=matrix[i][j]
        return newMatrix

solution = Solution()
print(solution.transpose([ [1,2,3], [4,5,6], [7,8,9] ]))