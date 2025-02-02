class Solution(object):
    def strStr(self, haystack, needle):
        index = haystack.find(needle)
        if index == -1:
            return -1
        else:
            return index
    @staticmethod
    def run():
        test_cases = [
            ("hello", "ll"),
            ("aaaaa", "bba"),
            ("abc", "c"),
            ("mississippi", "issip"),
            ("", ""),
            ("a", "a"),
        ]

        sol = Solution()
        for haystack, needle in test_cases:
            result = sol.strStr(haystack, needle)
            print(f"Haystack: '{haystack}', Needle: '{needle}', Index: {result}")

Solution.run()
