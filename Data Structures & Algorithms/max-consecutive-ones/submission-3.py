class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # keep a running total of max and update as you loop
        # check if max is 0 or not, then increment to 1 if one
        # then increment or reset as necessary

        max_ones = 0
        curr_ones = 0

        for num in nums:
            if num == 0:
                curr_ones = 0
            else:
                curr_ones += 1
            max_ones = max(curr_ones, max_ones)

        return max_ones