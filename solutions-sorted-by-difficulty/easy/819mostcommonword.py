import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        mapList = {}
        maxOccurence = 0
        maxWord = ""
        words = re.findall(r'\w+', paragraph.lower())

        for word in words:
            word = ''.join(c for c in word if c.isalnum())
            if word and word not in banned:
                mapList[word] = mapList.get(word, 0) + 1
                if mapList[word] > maxOccurence:
                    maxOccurence = mapList[word]
                    maxWord = word
        return maxWord

solution = Solution()
print(solution.mostCommonWord("a, a, a, a, b,b,b,c, c","a"))