class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # running count of consecutives 
        # compare old count to new count by taking max 
        # return max count 
        max_count, count = 0, 0
        for num in nums:
            if num == 0:
                count = 0
            else:
                count +=1
                max_count = max(max_count, count)
        return max_count