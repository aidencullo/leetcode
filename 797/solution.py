class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            if node in seen:
                return

            seen.append(node)

            if node == n - 1:
                paths.append(list(seen))
                seen.pop()
                return


            for neighbor in graph[node]:
                dfs(neighbor)

            seen.pop()


        paths = []
        seen = []
        n = len(graph)

        dfs(0)
        return paths
