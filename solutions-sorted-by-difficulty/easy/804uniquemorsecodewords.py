class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse_list = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
    "..-", "...-", ".--", "-..-", "-.--", "--.."
]

        morse_map = {chr(ord('a') + i): morse_list[i] for i in range(26)}
        unique_morse_codes = set()
        for word in words:
            morseWord=""
            for letter in word:
                morseWord+=morse_map[letter]
            unique_morse_codes.add(morseWord)
        return len(unique_morse_codes)

solution = Solution()
print(solution.uniqueMorseRepresentations(["gin","zen","gig","msg"]))

