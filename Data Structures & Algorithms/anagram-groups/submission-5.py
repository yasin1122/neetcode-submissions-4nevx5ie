from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each word and store as dict key
        # if sorted version matches key, append to list of vals
        # return all vals in dict as list of lists

        anagrams = defaultdict(list)

        for word in strs:
            anagrams["".join(sorted(word))].append(word)

        return list(anagrams.values())