from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # return 2d array of anagrams
        
        # loop through the list and sort each string
        # store each sorted string in a dictionary
        # key = sorted string, values = [list of original strings]
        # return dict.values() as a list

        anagram_dict = defaultdict(list)

        for s in strs:
            anagram_dict["".join(sorted(s))].append(s)

        return list(anagram_dict.values())