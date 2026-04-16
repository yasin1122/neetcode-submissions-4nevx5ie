class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # iterate and try to convert to int
        # if possible add it to new List
        # if not use if to pick and do the operations
        # return sum of the new arr

        stack = []

        for op in operations:
            try:
                stack.append(int(op))
            except:
                if op == '+':
                    stack.append(stack[-1] + stack[-2])
                elif op == 'D':
                    stack.append(stack[-1]*2)
                elif op == 'C':
                    stack.pop()
                else:
                    print("Something went wrong!")
        
        return sum(stack)
