class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # have a counter
        # take the max of current count and max
        # while you iterate through the list
        # return max

        counter = 0
        max_count = 0

        for num in nums:
            if num == 1:
                counter += 1
                max_count = max(max_count, counter)
            else:
                counter = 0

        return max_count