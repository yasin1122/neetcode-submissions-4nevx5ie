class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # traverse nums
            # key = target - num
            # value = [index, value]

            # if num is not key, we store
            # if num is key, we return both indices

        result_map = {}

        for i, n in enumerate(nums):
            if n not in result_map:
                result_map[target - n] = [i, n]
            else:
                ind = result_map[n]
                return [ind[0], i]