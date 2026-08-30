class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums).most_common(k)
        return [nums_count[i][0] for i in range(k)]