class Solution:
    def isValid(self, s: str) -> bool:
        # create an empty stack
        # create a map to avoid if statements
        # push opening chars to the stack
        # when closing char is encountered
            # if stack is empty return false
            # pop and check if it matches closing char
                # if not return false else continue
        # if stack is empty return true, else false

        stack = []
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char not in bracket_map:
                stack.append(char)
            elif stack and bracket_map[char] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return not stack