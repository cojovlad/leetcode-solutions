class Solution(object):
    def longestPalindrome(self, s):
        mapOfChars={}
        for char in s:
            mapOfChars[char]=mapOfChars.get(char,0)+1
        length=len(s)
        ok=0
        for item in mapOfChars:
            if mapOfChars[item]%2==0:
                continue
            else:
                if mapOfChars[item]%2==1 and ok==0:
                    ok=1
                    continue
                else:
                    length-=1
        return length

solution = Solution()
print(solution.longestPalindrome("bananas"))
