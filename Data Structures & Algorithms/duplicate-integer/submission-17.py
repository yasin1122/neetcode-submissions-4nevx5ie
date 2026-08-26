class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums)) != len(nums)
        
        # we can sort, then compare to prev
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        # use hashset

        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)

        return False
