class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total = 0

        for op in operations:
            if op == "+":
                total += record[-1] + record[-2]
                record.append(record[-1] + record[-2])
            elif op == "D":
                total += record[-1] * 2
                record.append(record[-1] * 2)
            elif op == "C":
                temp = record.pop()
                total -= temp
            else:
                record.append(int(op))
                total += int(op)

        return total
