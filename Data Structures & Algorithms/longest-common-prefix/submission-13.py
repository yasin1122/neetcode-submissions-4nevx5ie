class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # brute force
        # loop through chars in first word
        # loop through words, if ith char is not equal
        # return accumulated prefix

        prefix = ""

        for i, char in enumerate(strs[0]):
            for word in strs:
                if i >= len(word):
                    return prefix
                if char != word[i]:
                    return prefix
            prefix += char

        return prefix
                