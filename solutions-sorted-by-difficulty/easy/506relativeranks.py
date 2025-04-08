class Solution(object):
    def findRelativeRanks(self, score):

        mapOfRanks = {}
        copyOfScore = sorted(score, reverse=True)
        placement=0
        listOfScores=[]
        for copiedScore in copyOfScore:
            placement+=1
            mapOfRanks[copiedScore] = placement
        for ranking in score:
            if mapOfRanks[ranking]==1:
                listOfScores.append("Gold Medal")
            elif mapOfRanks[ranking]==2:
                listOfScores.append("Silver Medal")
            elif mapOfRanks[ranking]==3:
                listOfScores.append("Bronze Medal")
            else:
                listOfScores.append(str(mapOfRanks[ranking]))

        return listOfScores

solution = Solution()
print(solution.findRelativeRanks([10,3,8,9,4]))