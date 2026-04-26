class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return indices [i, j] that add up to target int
        # return smaller index first.
        # no edge cases

        # create a dictionary that stores target - curr_value : curr_index
        # loop over nums with an index
        # check if curr_value is in the index
            # if so, return the 2 indices, you can sort them
            # if not add to the dictionary target - curr_value : curr_index

        result = {}

        for i in range(len(nums)):
            if nums[i] in result:
                return sorted([i, result[nums[i]]])
            else:
                result[target - nums[i]] = i