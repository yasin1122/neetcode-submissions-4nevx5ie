class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        count = 1
        half = len(nums) // 2
        sorted_nums = sorted(nums)
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] != sorted_nums[i - 1]:
                count = 1
            else:
                count += 1
            if count > half:
                return sorted_nums[i]
        return 0