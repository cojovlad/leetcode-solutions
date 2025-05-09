class Solution(object):
    def reverseVowels(self, s):
        emptyList = []
        for letter in s:
            if letter in "aeiouAEIOU":
                emptyList.append(letter)

        result = ""
        for letter in s:
            if letter in "aeiouAEIOU":
                result += emptyList.pop()
            else:
                result += letter

        return result

solution = Solution()
print(solution.reverseVowels("IceCreAm"))
