class Solution(object):
    def findRestaurant(self, list1, list2):
        listOne={}
        listTwo={}
        for i,word in enumerate(list1):
            listOne[word]=i
        for i,word in enumerate(list2):
            listTwo[word]=i

        minim = 10 ** 18

        newList=[]
        for word in listOne:
            if word in listTwo:
                if listOne[word]+listTwo[word]<minim:
                    newList=[]
                    newList.append(word)
                    minim=listOne[word]+listTwo[word]
                elif listTwo[word]+listOne[word]==minim:
                    newList.append(word)
        return newList

solution = Solution()
print(solution.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Shogun","Burger King"]))