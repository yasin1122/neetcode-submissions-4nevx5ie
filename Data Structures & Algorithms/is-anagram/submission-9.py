class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we can sort the strings and see if they are equal
        # we can put it in a dictionary see if second str equals?

        s_map = Counter(s)

        for char in t:
            if char not in s_map:
                return False
            if char in s_map:
                if s_map[char] > 1:
                    s_map[char] -= 1
                else:
                    del s_map[char]

        return True if len(s_map) == 0 else False