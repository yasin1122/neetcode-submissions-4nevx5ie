class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check len equality first
        # count the char in s then t in a dict {char: count}
        # check if they are equal and return result
        
        if len(s) != len(t):
            return False

        def str_to_dict(string):
            str_map = {}

            for char in string:
                if char not in str_map:
                    str_map[char] = 1
                else:
                    str_map[char] += 1

            return str_map

        return str_to_dict(s) == str_to_dict(t)