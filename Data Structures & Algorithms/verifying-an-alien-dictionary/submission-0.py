class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # loop through the first word's chars
        # if the index on the order is greater than the first character of the next word
            # return False
        # else, move to the 2nd character if it exists

        return words == sorted(words, key=lambda word:[order.index(c) for c in word])


