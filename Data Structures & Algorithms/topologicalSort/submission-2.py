class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = {}
        for i in range(n):
            graph[i] = []

        for src, dst in edges:
            graph[src].append(dst)

        print('graph: ', graph)
        visited = set()
        path = set()
        order = []
        def dfs(n, v, p, o, g):
            if n in p:
                return False
            if n in v:
                return True
            print("n: ", n)
            v.add(n)
            p.add(n)
            for neigh in g[n]:
                if not dfs(neigh, v, p, o, g):
                    return False
            o.append(n)
            p.remove(n)

            return True

        for i in range(n):
            if not dfs(i, visited, path, order, graph):
                print("cycle")
                return []
        
        order.reverse()
        return order