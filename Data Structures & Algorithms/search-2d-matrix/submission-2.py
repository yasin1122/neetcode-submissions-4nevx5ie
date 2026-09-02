class Solution:
    def binary_search(self, arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if target < arr[m]:
                r = m - 1
            elif target > arr[m]:
                l = m + 1
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) - 1

        while start <= end:
            row = (start + end) // 2
            if target > matrix[row][-1]:
                start = row + 1
            elif target < matrix[row][0]:
                end = row - 1
            else:
                break
        
        if not (start <= end):
            return False

        row = (start + end) // 2
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
