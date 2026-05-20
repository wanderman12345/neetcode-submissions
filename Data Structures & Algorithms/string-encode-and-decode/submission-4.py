class Solution:

    def encode(self, strs: List[str]) -> str:
        return tuple(strs)

    def decode(self, s: str) -> List[str]:
        if s == []:
            return []
        out = []
        for eachWord in s:
            out.append(eachWord)
        return out

