class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 1
        while i < len(arr):
            arr[i - 1] = max(arr[i:])
            i += 1
        arr[-1] = -1
        return arr