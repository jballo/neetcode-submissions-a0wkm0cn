class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for src, dst in prerequisites:
            graph[src].append(dst)

        

        order = []
        visited = set()
        path = set()

        def dfs(i, o , g, v, p):
            if i in p:
                return False
            if i in v:
                return True

            p.add(i)
            for neigh in g[i]:
                if not dfs(neigh, o, g, v, p):
                    return False

            v.add(i)
            o.append(i)
            p.remove(i)
            return True
        

        for i in range(numCourses):
            if not dfs(i, order, graph, visited, path):
                return []

        return order
