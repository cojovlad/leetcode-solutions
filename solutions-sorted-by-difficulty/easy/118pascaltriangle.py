class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        if numRows == 3:
            return [[1], [1,1], [1,2,1]]
        nestedList =[[1], [1,1], [1,2,1]]
        usedRows=3
        while usedRows<numRows:
            nestedList.append([])
            nestedList[usedRows].append(1)
            innerList=nestedList[usedRows-1]
            for i in range(len(innerList)-1):
                nestedList[usedRows].append(innerList[i]+innerList[i+1])
            nestedList[usedRows].append(1)
            usedRows+=1
        return nestedList

solution = Solution()
print(solution.generate(40))