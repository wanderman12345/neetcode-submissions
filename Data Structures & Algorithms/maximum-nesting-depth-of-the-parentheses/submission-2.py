class Solution:
    def maxDepth(self, s: str) -> int:
        maxLength = 0
        c = 0
        for eachChar in s:
            if eachChar == "(":
                c += 1
                maxLength = max(maxLength, c)
            elif eachChar == ")":
                c -= 1
        
        return maxLength