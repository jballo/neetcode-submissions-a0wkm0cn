class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        
        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = set()
        path = set()
        def dfs(i, v, p, g):
            if i in p:
                return False
            if i in v:
                return True

            v.add(i)
            p.add(i)
            for pre in g[i]:
                if not dfs(pre, v, p, g):
                    return False
            
            p.remove(i)
            return True


        for i in range(numCourses):
            if not dfs(i, visited, path, graph):
                return False

        return True