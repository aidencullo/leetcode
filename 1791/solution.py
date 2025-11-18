class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(int)

        for edge in edges:
            u, v = edge

            graph[u] += 1
            graph[v] += 1

        n = len(graph)

        for node in graph:
            if graph[node] == n - 1:
                return node

        return -1
