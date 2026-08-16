class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # t needs to be a substring of s
        # i, j pointers move to compare chars
        # len(t) - j is the answer

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1

        return len(t) - j