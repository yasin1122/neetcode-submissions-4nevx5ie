class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # go through the first str
        for i in range(len(strs[0])):
            for s in strs[1:]: 
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]