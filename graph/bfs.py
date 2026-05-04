from collections import deque

class Solution:
    def bfs(self, adj):
        n = len(adj)
        visited = [False] * n
        queue = deque([0])
        
        visited[0] = True
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result