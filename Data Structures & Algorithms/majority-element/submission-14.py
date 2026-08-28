class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = None, 0

        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)

        return res

        # return Counter(nums).most_common(1)[0][0]

        nums.sort()

        return nums[len(nums) // 2]