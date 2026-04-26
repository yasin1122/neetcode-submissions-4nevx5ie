class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if there are any duplicates, return True, else, False

        # if len(set(nums)) != len(nums) then we have duplicates

        return len(set(nums)) != len(nums)