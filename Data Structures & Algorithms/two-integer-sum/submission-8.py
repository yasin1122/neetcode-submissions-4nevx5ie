class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate through the list
            # if dict is empty, fill the first KV pair
        # use a dictionary 
            # key = target - curr value
            # value = curr indicie
        # before that check curr exist in the dictionary
            # if so, return curr indicie, and the indicie in the dictionary
            # else keep going

        solution_map = {
            target - nums[0]: 0
        }

        for i in range(1, len(nums)):
            if nums[i] in solution_map:
                if i <= solution_map[nums[i]]:
                    return [i, solution_map[nums[i]]]
                else:
                    return [solution_map[nums[i]], i]
            else:
                solution_map[target - nums[i]] = i
            