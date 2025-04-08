class Solution(object):
    def findWords(self, words):
        newList=[]
        listOne=("qwertyuiop")
        listTwo=("asdfghjkl")
        listThree=("zxcvbnm")

        for word in words:
            lowerWord=set(word.lower())
            if lowerWord.issubset(listOne):
                newList.append(word)
            elif lowerWord.issubset(listTwo):
                newList.append(word)
            elif lowerWord.issubset(listThree):
                newList.append(word)

        return newList

solution = Solution()
print(solution.findWords(["Hello","Alaska","Dad","Peace"]))