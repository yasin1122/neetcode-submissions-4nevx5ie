class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # brute force
        # loop through chars in first word
        # loop through words, if ith char is not equal
        # return accumulated prefix

        prefix = ""

        # for i, char in enumerate(strs[0]):
        #     for word in strs:
        #         if i >= len(word) or char != word[i]:
        #             return prefix
        #     prefix += char

       

        if len(strs) == 1:
            return strs[0]
                
        strs.sort()

        for i, char in enumerate(strs[0]):
            if char == strs[-1][i]:
                prefix += char
            else:
                return prefix

        return prefix