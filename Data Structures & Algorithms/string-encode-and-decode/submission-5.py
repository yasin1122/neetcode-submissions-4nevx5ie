class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1 and strs[0] == "":
            return "\"\""
        return "~!@#$".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "\"\"":
            return [""]
        return [] if len(s) == 0 else s.split("~!@#$")