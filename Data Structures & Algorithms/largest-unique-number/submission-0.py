class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # we can turn nums into a Counter dict
        # delete keys that have duplicates
        # return the max of the leftover unique vales
        # if len(left over keys) is 0 return -1

        nums_map = Counter(nums)
        unique_nums = []

        for num, count in nums_map.items():
            if count == 1:
                unique_nums.append(num)

        return -1 if len(unique_nums) == 0 else max(unique_nums)
