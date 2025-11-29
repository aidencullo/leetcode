from collections import defaultdict, deque
from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()
        q = deque([source])

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == destination:
                    return True
                seen.add(node)
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        q.append(neighbor)

        return False
