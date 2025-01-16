class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        if not strs:
            return ""

        new = ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        for i in range(len(first)):
            if i<len(last) and first[i]==last[i]:
                new+=first[i]
            else:
                break
        return new

    @staticmethod
    def run():
        strs = input("Enter a list of strings separated by commas: ").split(',')
        strs = [s.strip() for s in strs]
        solution = Solution()
        result = solution.longestCommonPrefix(strs)
        print(f"Longest Common Prefix: '{result}'")

Solution.run()
