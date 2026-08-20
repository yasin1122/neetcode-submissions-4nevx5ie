class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # join arr into a str
        # split on spaces back into an arr
        # reverse the arr

        s[:] = list(" ".join("".join(s).split(" ")[::-1]))
        
