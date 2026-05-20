class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # split into substrings and checkpalindrome
        def isPalindrome(s,i,j):
            return s[i:j+1] == s[i:j+1][::-1]
        res = []
        part = []

        def DFS(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(s,i,j):
                    part.append(s[i:j+1])
                    DFS(j+1)
                    part.pop()
                
        DFS(0)
        return res

    
            
        


        