class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        num_counter = Counter()
        common_nums = []

        for row in mat:
            num_counter.update(row)

        for num, count in num_counter.items():
            if count == len(mat):
                common_nums.append(num)
        
        if len(common_nums) == 0:
            return -1
        
        return sorted(common_nums)[0]