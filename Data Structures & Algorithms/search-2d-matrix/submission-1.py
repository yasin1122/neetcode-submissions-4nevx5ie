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
        return self.binary_search([el for row in matrix for el in row], target)