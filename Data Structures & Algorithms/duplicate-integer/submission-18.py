class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # store numbers in a hash_set
        # check if num is in set while looping
        # if it is return true, false at the end of func

        hash_set = set()

        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)

        return False