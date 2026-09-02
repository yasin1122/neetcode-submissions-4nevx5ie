import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x, y in points:
            distance = x ** 2 + y ** 2
            heapq.heappush(min_heap, [distance, [x, y]])

        k_closest = []

        while k > 0:
            distance, point = heapq.heappop(min_heap)
            k_closest.append(point)
            k -= 1

        return k_closest