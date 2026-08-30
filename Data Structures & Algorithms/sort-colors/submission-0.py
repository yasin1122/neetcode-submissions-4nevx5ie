class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_map = { 0 : 0, 1 : 0, 2 : 0 }

        for num in nums:
            color_map[num] += 1

        i = 0
        for color, count in color_map.items():
            for _ in range(count):
                nums[i] = color
                i += 1
            
