class Solution(object):
    def isAnagram(self, s, t):
        if(len(s) != len(t)):
            return False
        firstHash={}
        secondHash={}
        for letter in s:
            firstHash[letter]=firstHash.get(letter,0)+1
        for letter in t:
            secondHash[letter]=secondHash.get(letter,0)+1

        for element in firstHash:
            if firstHash[element] != secondHash.get(element, 0):
                return False
        return True

solution = Solution()
print(solution.isAnagram("car","rac"))