class Solution:
    def isValid(self, s: str) -> bool:
        # create an empty stack
        # add opening chars to stack
        # pop when closing char
        # check if they match if not return False
        # stack is empty then return True
        # otherwise false
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif char == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif char == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif char == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False

        return not stack