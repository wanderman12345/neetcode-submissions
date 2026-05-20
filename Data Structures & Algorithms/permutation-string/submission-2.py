class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w2 = Counter (s1)
        s = set(s1)
        l = 0
        out = False
        r = len(s1)-1
        while r < len(s2):
            if s2[r] in s:
                if Counter(s2[l:r+1]) == w2:
                    out = True

            l += 1
            r += 1

        return out
            
