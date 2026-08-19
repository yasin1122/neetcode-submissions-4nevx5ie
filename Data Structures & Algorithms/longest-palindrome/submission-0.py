from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # the middle could be 1 odd char or 0
        # everything else has to be in pairs
        # we can count the chars in a dictionary
        # we can mod 2 the counts and add to length the result
        # also we can add at most 1 odd count if such exist

        char_map = Counter(s)

        longest_length = 0

        for count in char_map.values():
            if count > 1:
                longest_length += (count // 2) * 2

        if char_map.total() > longest_length:
            longest_length += 1

        return longest_length