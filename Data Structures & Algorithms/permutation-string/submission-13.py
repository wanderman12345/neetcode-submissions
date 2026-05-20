class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w2 = Counter (s1)
        s = set(s1)
        l = 0
        out = False
        r = len(s1)-1
        globalC = Counter(s2[l:r+1])
        while r < len(s2):
            print(globalC)
            if s2[r] in s:
                if globalC == w2:
                    out = True
            if globalC[s2[l]] > 0:
                globalC[s2[l]] -= 1
            else:
                del globalC[s2[l]]
            l += 1
            r += 1
            if r < len(s2):
                globalC[s2[r]] += 1

        return out




            
