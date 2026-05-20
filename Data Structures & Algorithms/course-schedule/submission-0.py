class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # create adjacency list
        preMap = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            preMap[crs].append(preq)

        # using DFS check if prereq met
        visited = set()
        def DFS(node):
            if preMap[node] == []:
                return True
            if node in visited:
                return False
            visited.add(node)
            for eachPreq in preMap[node]:
                if not DFS(eachPreq):
                    return False
            visited.remove(node)    
            return True
    
        for c in range(numCourses):
            if not DFS(c):
                return False
        return True

