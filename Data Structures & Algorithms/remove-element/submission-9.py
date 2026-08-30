class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # remove all vals in place and return count of non vals
        # start, end pointers. 
        # if start == val, swap with end, decrement end
        # if start != val, then increment start
        # if start == end, exit loop, return start

        start, end = 0, len(nums) - 1

        while start <= end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1

        return start