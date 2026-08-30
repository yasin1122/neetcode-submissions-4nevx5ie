class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # start from the end, compare curr to old max, store in i
        rightMax = float('-inf')

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax

        arr[-1] = -1
        return arr


        i = 1
        while i < len(arr):
            arr[i - 1] = max(arr[i:])
            i += 1
        arr[-1] = -1
        return arr