class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # we can zip the 2 lists together
        # sort by heights reversed=True
        # return just the names

        height_name_pairs = list(zip(heights, names))
        height_name_pairs.sort(reverse=True)

        return [pair[1] for pair in height_name_pairs]