class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def checkPermutation(w1, w2):
            return Counter(w1) == Counter(w2)

        l = 0
        out = False
        r = len(s1)-1
        while r < len(s2):
            if checkPermutation(s2[l:r+1], s1):
                out = True

            l += 1
            r += 1

        return out
            
