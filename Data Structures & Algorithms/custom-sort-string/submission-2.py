class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # map each char in order to a rank, with enumerate
        # sort "s" with rank of char, 
        # helper func, return rank or len(order)(because greater than last)

        rank_map = {}

        for i, char in enumerate(order):
            rank_map[char] = i

        def get_rank(char):
            if char in rank_map:
                return rank_map[char]
            else:
                return len(order)
        
        ranked_s = sorted(s, key = get_rank)

        return "".join(ranked_s)