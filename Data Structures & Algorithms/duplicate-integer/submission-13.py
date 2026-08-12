class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # loop through the array
            # check if num in in a set
                # if it is return True
                # else add it to set
        # if no duplicates found, return False

        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        
        return False