class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # {"c": 0, "b": 1, ...}
        rank = {char: i for i, char in enumerate(order)}

        # result = sorted(s, key=lambda c: rank.get(c, len(order)))

        def get_character_rank(character):
            if character in rank:
                return rank[character]
            else:
                return len(order)

        result = sorted(s, key=get_character_rank)

        return "".join(result)
