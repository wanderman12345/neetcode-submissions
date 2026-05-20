class Solution:
    def numDecodings(self, s: str) -> int:
        alpha = {
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5',
    'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '10',
    'K': '11', 'L': '12', 'M': '13', 'N': '14', 'O': '15',
    'P': '16', 'Q': '17', 'R': '18', 'S': '19', 'T': '20',
    'U': '21', 'V': '22', 'W': '23', 'X': '24', 'Y': '25',
    'Z': '26'
}
        memo = {}
        def dfs(n):
            if n > len(s):
                return 0
            if n == len(s):
                return 1
            if s[n] == '0':
                return 0
            if n in memo:
                return memo[n]
            # size one or size two
            else:
                char1 = s[n:n+1]
                char2 = s[n:n+2]
                res = dfs(n+1)
                memo[n] = res
                if n+1 < len(s) and 10 <= int(s[n:n+2]) <= 26:
                    res += dfs(n+2)
                    memo[n] = res
                return res
                
        return dfs(0)


