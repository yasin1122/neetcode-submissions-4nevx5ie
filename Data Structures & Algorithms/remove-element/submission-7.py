class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        start = 0
        end = len(nums)

        # will exit with no edge cases
        while start < end:
            # we only iterate the end if it IS val and SWAP
            if nums[start] == val:
                end -= 1
                nums[start] = nums[end]
            # we only iterate start if num is NOT val
            else:
                start += 1
        
        return start
                
"""
11211 1
11211
21111
21111

start = 1
"""