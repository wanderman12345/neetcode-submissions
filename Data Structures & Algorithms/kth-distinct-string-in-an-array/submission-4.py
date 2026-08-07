class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        unique = set()
        order = []
        duplicate = set()
        for alpha in arr:
            if alpha in unique:
                duplicate.add(alpha)
            unique.add(alpha) 
        
        u = unique - duplicate

        count = 0 
        for i in range(len(arr)):
            if arr[i] in u:
                count += 1
            if count == k:
                return arr[i]
       
        return ""
        