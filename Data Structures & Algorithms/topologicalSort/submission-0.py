class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}

        for i in range(n):
            graph[i] = []

        for src, dst in edges:
            graph[src].append(dst)
        

        visited = set()
        path = set()
        order = []
        for i in range(n):
            if not self.dfs(graph, i, order, visited, path):
                return []
        order.reverse()
        return order
    
    def dfs(self, g, i, o, v, p):
        if i in p:
            return False
        if i in v:
            return True
        v.add(i)
        p.add(i)
        for neigh in g[i]:
            if not self.dfs(g, neigh, o, v, p):
                return False
        o.append(i)
        p.remove(i)
        return True