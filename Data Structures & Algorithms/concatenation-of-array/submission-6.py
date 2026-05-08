class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans = [0] * (nums_len * 2)

        for i in range(nums_len):
            ans[i] = ans[i + nums_len] = nums[i]

        return ans