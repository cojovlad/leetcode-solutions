class Solution(object):
    def diagonalSum(self, mat):
        R,C = len(mat), len(mat[0])
        sumMatirx=0
        for i in range(C):
            for j in range(R):
                if i == j:
                    sumMatirx+=mat[i][j]
                if i+j == C-1:
                    sumMatirx+=mat[i][j]
        if(C%2==0):
            return sumMatirx
        else:
            return sumMatirx-mat[C//2][C//2]

solution = Solution()
print(solution.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))