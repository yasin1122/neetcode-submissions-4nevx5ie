class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # turn magazine into a Counter
        # loop over ransomNote and deduct from Counter
        # if we can't return False, 
        # after to loop return True

        magazine_map = Counter(magazine)

        for char in ransomNote:
            if char not in magazine_map or magazine_map[char] == 0:
                return False
            else:
                magazine_map[char] -= 1
        
        return True