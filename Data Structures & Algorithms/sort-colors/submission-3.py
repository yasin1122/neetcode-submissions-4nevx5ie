class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_list = [0, 0, 0]

        for num in nums:
            color_list[num] += 1

        i = 0
        for color, count in enumerate(color_list):
            for _ in range(count):
                nums[i] = color
                i += 1
            
