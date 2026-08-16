class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # {"c": 0, "b": 1, ...}
        rank = {char: i for i, char in enumerate(order)}

        result = sorted(s, key=lambda c: rank.get(c, len(order)))

        return "".join(result)
