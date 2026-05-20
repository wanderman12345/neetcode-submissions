class Solution:
    def scoreOfString(self, s: str) -> int:
        # go through string and obtain val from taking substring of size two getting abs diff and adding to final
        total = 0
        for i in range(len(s)):
            if i+1 < len(s):
                total += abs(ord(s[i])-ord(s[i+1]))
        return total
        