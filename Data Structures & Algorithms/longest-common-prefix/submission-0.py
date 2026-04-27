class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''

        for col in zip(*strs):
            if len(set(col)) == 1:
                result += col[0]
            else:
                return result

        return result