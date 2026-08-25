class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # create ans array 
        # ans = nums + nums, then return it

        # ans = [0] * len(nums) * 2
        # for i, num in enumerate(nums):
        #     ans[i] = num
        #     ans[i + len(nums)] = num
        # return ans

        return nums * 2