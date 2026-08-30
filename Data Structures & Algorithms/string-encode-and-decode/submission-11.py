class Solution:

    def encode(self, strs: List[str]) -> str:
        strs_list = []
        for word in strs:
            strs_list.append(str(len(word)) + "#" + word)
        return "".join(strs_list)

    def decode(self, s: str) -> List[str]:
        word_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j]) # len of a word
            i = j + 1 
            j = i + length
            word_list.append(s[i:j])
            i = j

        return word_list
