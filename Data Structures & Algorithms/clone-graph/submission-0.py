"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adjList = {}
        visited = set()

        def dfs(node):
            if node == None:
                return None
            if node in visited:
                return adjList[node]
            
            newNode = Node(node.val)
            adjList[node] = newNode
            visited.add(node)
            for neigh in node.neighbors:
                adjList[node].neighbors.append(dfs(neigh))

            return newNode
            
        return dfs(node)

        