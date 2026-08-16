class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # we can loop through the outer list
        # look at ONLY the 1st and last element
        # set new min and max accordingly
        # return the abs(max - min)

        min_val, max_val = arrays[0][0], arrays[0][-1]
        res = 0

        for array in arrays[1:]:
            res = max(res, array[-1] - min_val, max_val - array[0])
            min_val = min(array[0], min_val)
            max_val = max(array[-1], max_val)

        return res