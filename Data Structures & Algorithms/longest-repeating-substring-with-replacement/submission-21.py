class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        maxLength = 1
        Count = {}
        for eachChar in s:
            Count[eachChar] = 0

        while r < len(s):
            length = r-l+1
            Count[s[r]] += 1
            maxCount = length - max(Count.values())
            if maxCount <= k:
                maxLength = max(maxLength, length)
                r += 1
            else:
                Count[s[l]] -= 1
                l += 1
                r += 1


        return maxLength








        