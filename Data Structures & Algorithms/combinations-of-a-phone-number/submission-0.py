class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        track = {2 : 'abc', 3 : 'def', 4: 'ghi', 5 : 'jkl', 6 : 'mno', 7 : 'pqrs', 8 : 'tuv', 9: 'wxyz'}
        out = []

        def backtrack(i, sub):
            if len(sub) == len(digits):
                out.append(sub)
            if i >= len(digits):
                return
            letterList = track[int(digits[i])]
            for j in range(len(letterList)):
                backtrack(i+1, sub + letterList[j])
            
        if digits:
            backtrack(0, "")

        return out


    #       []
    #     d     e    f
    #  g h i  g h i g h i
