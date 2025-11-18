class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(int)
        nodes = set()
        

        for edge in edges:
            u, v = edge

            nodes.add(u)
            nodes.add(v)

        n = len(nodes)

        for edge in edges:
            u, v = edge

            graph[u] += 1
            graph[v] += 1

            if graph[u] == n - 1:
                return u
            if graph[v] == n - 1:
                return v
