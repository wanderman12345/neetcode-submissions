class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      l = 0
      r = 0
      unique = set()
      localLength  = 0
      maxLength = 0
      while r < len(s):
        if s[r] not in unique:
            unique.add(s[r])
            localLength += 1

        else:
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
                localLength -= 1
            unique.add(s[r])
            localLength += 1
            

        maxLength = max(maxLength, localLength)
        r += 1

      return maxLength








        
        