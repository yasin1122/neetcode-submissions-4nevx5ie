# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s + 1 <= 1: # if length = 1, its already sorted
            return pairs

        m = (s + e) // 2 # floor division to find the middle

        self.mergeSortHelper(pairs, s, m) # sort the left half
        self.mergeSortHelper(pairs, m + 1, e) # sort the right half

        self.merge(pairs, s, m, e) # merging back the sorted halves

        return pairs

    # merge 2 sorted halves in place
    def merge(self, arr: List[Pair], s: int, m: int, e: int) -> None:
        # Copy sorted left & right halves
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        i = j = 0 # indexes for L & R, respectively
        k = s # starting index for arr

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while k < len(arr):
            if i < len(L):
                arr[k] = L[i]
                i += 1
            elif j < len(R):
                arr[k] = R[j]
                j += 1
            k += 1
