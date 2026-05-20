class Solution:

    def encode(self, strs: List[str]) -> str:
        # concatenate all strings with a NON UTF-8 char
        out = ""
        if strs == []:
            return "[]"
        for eachWord in strs:
            out = out + eachWord + "À"

        return out[:-1]
    def decode(self, s: str) -> List[str]:
        # separate all strings based of NON UTF-8 char
        out = []
        if s == "[]":
            return []
        words = s.split("À")
        for eachWord in words:
            out.append(eachWord)
        
        return out
