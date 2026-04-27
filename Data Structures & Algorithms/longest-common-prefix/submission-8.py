class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # loop through the first str
        # check if other str(s) match char by char
        # return str[:i] or str if loop is done

        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i == len(s) or strs[0][i] != s[i]:
                    return strs[0][:i]
        
        return strs[0]