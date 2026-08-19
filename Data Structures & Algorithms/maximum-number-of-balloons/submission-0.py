class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # count the chars in text
        # initialize count to 0
        # if chars to form balloon can be extracted, increment count
        # else return count

        text_map = Counter(text)
        balloon_count = 0

        while True:
            for char in "balloon":
                if text_map[char] > 0:
                    text_map[char] -= 1
                else:
                    return balloon_count

            balloon_count += 1