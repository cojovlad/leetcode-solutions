class Solution(object):
    

    def modifiedMatrix(self, matrix):
        R,C = len(matrix), len(matrix[0])
        for i in range(C):
            maxNumber=0
            for j in range(R):
                if matrix[j][i] != -1:
                    maxNumber = max(maxNumber, matrix[j][i])

            for j in range(R):
                if matrix[j][i] == -1:
                    matrix[j][i] = maxNumber
        return matrix

solution = Solution()
print(solution.modifiedMatrix([[-1,0,0,2,2],[2,0,0,2,1],[4,3,2,1,1],[-1,3,0,2,4],[1,0,3,2,0]]))