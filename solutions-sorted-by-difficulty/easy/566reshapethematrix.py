class Solution(object):
    def matrixReshape(self, mat, r, c):
        m,n=len(mat),len(mat[0])
        if(m*n) != (r*c):
            return mat
        newMat=[[0]*c for _ in range(r)]
        row=col=0

        for i in range(m):
            for j in range(n):
                newMat[row][col]=mat[i][j]
                col+=1
                if(col==c):
                    col=0
                    row+=1
        return newMat

solution = Solution()
print(solution.matrixReshape([[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]],3,3))
