class Solution:
    def encode(self, strs: List[str]) -> str:
        # concatenate all strings with a NON UTF-8 char
        out = ""
        if strs == []:
            return "[]"
        for eachWord in strs:
            out = out + str(len(eachWord)) + "#" + eachWord
        return out
        
    def decode(self, s: str) -> List[str]:
        # separate all strings based of NON UTF-8 char
        out = []
        if s == "[]":
            return []
       
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            num = int(s[i:j])
            i = j + 1
            j = i + num
            word = s[i:j]
            out.append(word)
            i = j
            
        return out
