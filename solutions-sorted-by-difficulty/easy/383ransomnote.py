class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomCount={}
        magazineCount={}
        for char in ransomNote:
            ransomCount[char]=ransomCount.get(char,0)+1
        for char in magazine:
            magazineCount[char]=magazineCount.get(char,0)+1

        for char in ransomCount:
            if ransomCount[char]>magazineCount[char]:
                return False
        return True

solution = Solution()
print(solution.canConstruct("aa","ab"))
