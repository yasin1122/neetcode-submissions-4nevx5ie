class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for string in strs:
            encoded_str += str(len(string)) + "@" + string
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # find @, what comes before it is length
        # extract length as int
        # slice word and add it to list to return
        word_list = []
        i, j, length = 0, 0, 0

        while j < len(s):
            if s[j] != '@':
                j += 1
            else:
                length = int(s[i:j])
                i = j + 1
                j = i + length
                word_list.append(s[i:j])
                i = j

        return word_list