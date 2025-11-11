class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            if node in seen:
                return

            if node == n - 1:
                seen.append(node)
                paths.append(list(seen))
                seen.pop()
                return

            seen.append(node)

            for neighbor in graph[node]:
                dfs(neighbor)

            seen.pop()


        paths = []
        seen = []
        n = len(graph)

        dfs(0)
        return paths
