class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [[0,1], [1, 3], [3,0]]
        # are we allowed to use other data structures?
        # are there any space or time constraints?

        # { 0: [1], 1: [3], 3: []}
        visited = set()

        courseAdjList = {}

        for crs in range(numCourses):
            courseAdjList[crs] = []

        for crs, pre in prerequisites:
            courseAdjList[crs].append(pre)

        for crs in range(numCourses):
            if not self.dfs(crs, courseAdjList, set()):
                return False
        
        return True

    def dfs(self, crs, adjList, visited):
        if adjList[crs] == []:
            return True
        elif crs in visited:
            return False
        
        visited.add(crs)
        for pre in adjList[crs]:
            if not self.dfs(pre, adjList, visited):
                return False
        visited.remove(crs)
        adjList[crs] = []
        return True