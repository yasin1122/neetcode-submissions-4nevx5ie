class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # we can loop over chars in t 
        # until we have a match at s[0]
        # then see if s matches the slice of t of same length
        # check if t has enough length
        # if so move on
        # if loop ends with no match, return false

        j = 0
        for i, char in enumerate(t):
            if j < len(s) and t[i] == s[j]:
                j += 1
        
        if j == len(s):
            return True

        return False
                