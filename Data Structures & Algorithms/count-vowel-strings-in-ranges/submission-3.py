class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # list of words, and list of inclusive ranges
        # count each word with vowel in range
        # return a list of counts
        vowels = {'a', 'e', 'i', 'o', 'u'}

        result = [0 for _ in range(len(queries))]
        i = 0

        for start, end in queries:
            for word in words[start : end + 1]:
                beg, end = False, False
                for vowel in vowels:
                    if vowel == word[0]:
                        beg = True
                    if vowel == word[-1]:
                        end = True
                if beg and end:
                    result[i] += 1
            i += 1
        
        return result

