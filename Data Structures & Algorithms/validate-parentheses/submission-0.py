class Solution:
    def isValid(self, s: str) -> bool:
        pair_dict = {")": "(", "}": "{", "]": "["}
        stack = []

        for ch in s:
            if ch in pair_dict:
                if stack and pair_dict[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return not stack
                