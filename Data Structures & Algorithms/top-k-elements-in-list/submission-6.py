class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        freq_list = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            nums_count[num] = 1 + nums_count.get(num, 0)
        
        for num, count in nums_count.items():
            freq_list[count].append(num)

        top_k = []
        for i in range(len(freq_list) - 1, 0, -1):
            for num in freq_list[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k


        # return [Counter(nums).most_common(k)[i][0] for i in range(k)]