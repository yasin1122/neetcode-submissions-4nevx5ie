class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for char in s:
            if char not in open_to_close:
                stack.append(char)
            elif stack and stack[-1] == open_to_close[char]:
                stack.pop()
            else:
                return False

        return not stack