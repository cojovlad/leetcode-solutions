class Solution(object):
    def firstUniqChar(self, s):
        dict={}
        for ch in s:
            dict[ch]=dict.get(ch,0)+1
        for i,element in enumerate(s):
            if dict[element]==1:
                return i
        return -1

solution = Solution()
print(solution.firstUniqChar("aabb"))
