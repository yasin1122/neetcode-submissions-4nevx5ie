# use a set to keep track of unique nums
# return set[0]
# add to both queue and set

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.uniques = defaultdict(int)

        for num in self.nums:
            self.uniques[num] += 1

    def showFirstUnique(self) -> int:
        for value, count in self.uniques.items():
            if count == 1:
                return value

        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        self.uniques[value] += 1
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
