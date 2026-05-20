class Solution:

    def encode(self, strs: List[str]) -> str:     
        out = ""
        for eachWord in strs:
            length = len(eachWord)
            out = out + str(length) + "#" + eachWord

        return out

    def decode(self, s: str) -> List[str]:
        print(s)
        out = []
        i = 0
        val = ""
        while i < len(s):
            if s[i] == "#":
                length = int(val)
                print(length)
                out.append(s[i+1:length+i+1])
                i = length+i+1
                val = ""
            else:
                val += s[i]
                i += 1
            
        return out
    