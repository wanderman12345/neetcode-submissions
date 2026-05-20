class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        unique = set()
        out = []
        def backtrack(i, sub):
            if sum(sub) == target and tuple(sorted(sub)) not in unique:
                unique.add(tuple(sorted(sub)))
                out.append((sorted(sub)))
                return
            elif sum(sub) > target:
                return
            else:
                for j in range(i, len(candidates)):
                    sub.append(candidates[j])
                    backtrack(j+1,sub)
                    sub.pop()
            
        backtrack(0, [])
        return out
                