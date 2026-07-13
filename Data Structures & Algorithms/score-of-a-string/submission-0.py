class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            first = s[i - 1]
            second = s[i]

            ascii_first = ord(first)
            ascii_second = ord(second)

            diff = abs(ascii_second - ascii_first)
            score += diff
        return score

        
        