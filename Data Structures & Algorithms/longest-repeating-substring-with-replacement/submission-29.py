class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        maxLength = 1
        Count = {}
        for eachChar in s:
            Count[eachChar] = 0

        while r < len(s):
            Count[s[r]] += 1
            while (r - l + 1 - max(Count.values())) > k:
                Count[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r-l+1)
            r += 1

        return maxLength
