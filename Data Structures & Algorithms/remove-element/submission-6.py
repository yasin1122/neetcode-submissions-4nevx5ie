class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[j] = nums[i]
        #         j += 1
        # return j

        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        return n

    
"""
 We use 2 pointers, the slow pointer doesn't move when nums[i] == val
 When nums[i] != val, we swap to erase val, and increment slow pointer j
 We return j, which is all the non val nums 
 Time = O(n) Space = O(1)
"""