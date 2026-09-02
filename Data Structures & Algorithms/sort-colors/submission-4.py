class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]

        for num in nums:
            colors[num] += 1

        k = 0
        for i, count in enumerate(colors):
            for _ in range(count):
                nums[k] = i
                k += 1