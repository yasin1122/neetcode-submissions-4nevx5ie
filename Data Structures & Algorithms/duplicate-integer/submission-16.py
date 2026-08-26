class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums)) != len(nums)
        
        # we can sort, then compare to prev

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False
