from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # return 2d array of anagrams
        
        # loop through the list and sort each string
        # store each sorted string in a dictionary
        # key = sorted string, values = [list of original strings]
        # loop through dict and append values to result list
        # return result list of lists

        anagram_dict = defaultdict(list)
        result = []

        for s in strs:
            anagram_dict["".join(sorted(s))].append(s)

        for vals in anagram_dict.values():
            result.append(vals)

        return result