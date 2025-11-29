class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()

        def dfs(node):

            if node in seen:
                return

            if node == destination:
                return True

            seen.add(node)

            return any(dfs(neighbor) for neighbor in graph[node])

        return dfs(source)


        
