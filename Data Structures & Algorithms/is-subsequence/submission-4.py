class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # we can use i, j to iterate over chars in s and t
        # at the end if we can't get to the last char in s
        # we return false
        # we only increment s if its matching char at t

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return True if i == len(s) else False