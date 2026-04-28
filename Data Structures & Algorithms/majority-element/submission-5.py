class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # voting system
        # count up or down for curr element, 
         # if vote = 0, new curr
         # majority vote survives, return it

        count = curr = 0

        for num in nums:
            if count == 0:
                curr = num
                count = 1
            if num == curr:
                count += 1
            else:
                count -= 1

        return curr