class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # build an adjacency list, go through using DFS, if cycle detected return False 
        adjList = defaultdict(list)
        for c,p in prerequisites:
            adjList[c].append(p)

        def DFS(n, s):
            if n in s:
                return False
            
            s.add(n)
            if n in adjList.keys():
                for p in adjList[n]:
                    if not DFS(p, s):
                        return False
    
            s.remove(n)
            return True

        for c in adjList.keys():
            s = set()
            if not DFS(c, s):
                return False

        return True

            
        
        


