class Solution:
    def numDecodings(self, s: str) -> int:
        self.out = 0
        alpha = {
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5',
    'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '10',
    'K': '11', 'L': '12', 'M': '13', 'N': '14', 'O': '15',
    'P': '16', 'Q': '17', 'R': '18', 'S': '19', 'T': '20',
    'U': '21', 'V': '22', 'W': '23', 'X': '24', 'Y': '25',
    'Z': '26'
}
        def dfs(n):
            if n == len(s):
                self.out += 1
                return
            elif n > len(s):
                return
            # size one or size two
            else:
                char1 = s[n:n+1]
                char2 = s[n:n+2]
                if char1 in alpha.values():
                    dfs(n+1)
                if char2 in alpha.values():
                    dfs(n+2)

        dfs(0)
        return self.out


