from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each word and store as dict key
        # if sorted version matches key, append to list of vals
        # return all vals in dict as list of lists

        anagrams = defaultdict(list)

        # for word in strs:
        #     anagrams["".join(sorted(word))].append(word)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            anagrams[tuple(count)].append(word)

        return list(anagrams.values())
        