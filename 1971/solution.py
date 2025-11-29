from collections import defaultdict
from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node: int) -> bool:
            if node in visited:
                return False

            visited.add(node)

            if node == destination:
                return True

            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True

            return False

        return dfs(source)
