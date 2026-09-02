import math

class Solution:
    def distance(self, p):
        return math.sqrt(((p[0] - 0) ** 2) + ((p[1] - 0) ** 2))

    def quicksort(self, arr, s, e):
        if s >= e:
            return arr

        left = s
        # pivot = arr[e]

        for i in range(s, e):
            if self.distance(arr[i]) < self.distance(arr[e]):
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
        arr[left], arr[e] = arr[e], arr[left]

        self.quicksort(arr, s, left - 1)
        self.quicksort(arr, left + 1, e)

        return arr

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quicksort(points, 0, len(points) - 1)[:k]