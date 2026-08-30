class Solution:
    def isValid(self, s: str) -> bool:

        bracket_stack = []

        for bracket in s:
            if bracket in "{[(":
                bracket_stack.append(bracket)
            elif len(bracket_stack) == 0:
                return False
            elif 1 <= ord(bracket) - ord(bracket_stack[-1]) <= 2:
                bracket_stack.pop()
            else:
                return False

        return True if len(bracket_stack) == 0 else False