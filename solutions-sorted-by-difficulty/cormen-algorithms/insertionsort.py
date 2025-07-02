class Solution(object):
    def insertionSort(self, numRows):
        for j in range(1, len(numRows)):
            key=numRows[j]
            i=j-1
            while i>= 0 and key<numRows[i]:
                numRows[i+1]=numRows[i]
                i-=1
            numRows[i+1]=key
        return numRows


solution = Solution()
print(solution.insertionSort([5,2,4,6,1,3]))