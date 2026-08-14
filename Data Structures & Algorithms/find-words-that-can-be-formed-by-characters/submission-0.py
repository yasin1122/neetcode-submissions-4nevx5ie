# list of word, and chars as str, 
# return len total of all words combined that can be formed by chars
# loop over words, check if each char in word is in chars
# if yes, add len to total
# return total lengths
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        chars_map = Counter(chars)

        for word in words:
            word_map = Counter(word)
            if word_map <= chars_map:
                total += len(word)

        return total