class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # split pattern into a list of words
        # store char : word
        # is the char in dict? does the value match?, then ok
        # if not return false
        # if we reach the end of both and false wasn't returned
        # return true

        s_list = s.split()
        pattern_map = {}

        if len(s_list) != len(pattern):
            return False

        for i, word in enumerate(s_list):
            if pattern[i] not in pattern_map:
                if word in pattern_map.values():
                    return False
                pattern_map[pattern[i]] = word
            elif pattern_map[pattern[i]] != word:
                return False

            #     char = pattern[i]
            # if char not in pattern_map:
            #     if word in pattern_map.values():
            #         return False
            #     pattern_map[char] = word
            # elif pattern_map[char] != word:

        return True
