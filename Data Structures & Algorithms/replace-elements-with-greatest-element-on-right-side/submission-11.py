class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # start from the end, compare curr to old max, store in i
        prev_max = -1
        i = len(arr) - 1
        while i >= 0:
            curr_max = max(prev_max, arr[i])
            arr[i] = prev_max
            prev_max = curr_max
            i -= 1
        
        return arr


        i = 1
        while i < len(arr):
            arr[i - 1] = max(arr[i:])
            i += 1
        arr[-1] = -1
        return arr