class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ""
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s):
                print(s[l:r+1])
                if s[l] == s[r]:
                    if len(s[l:r+1]) > len(out):
                        out = (s[l:r+1])
                    l -= 1
                    r += 1
                else:
                    break
            l = i
            r = i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if len(s[l:r+1]) > len(out):
                        out = (s[l:r+1])
                    l -= 1
                    r += 1
                else:
                    break
        return out
