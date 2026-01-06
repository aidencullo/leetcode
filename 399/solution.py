class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(dict)

        for i, (a, b) in enumerate(equations):
            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]

        res = []

        def find_query(start, end):
            product = -1

            if start not in graph or end not in graph:
                return product

            seen = set()

            def dfs(node, running):
                if node == end:
                    product = running
                    return

                seen.add(node)
                
                for neighbor, val in graph[node].values():
                    if neighbor not in seen:
                        dfs(neighbor, running + val)

            dfs(start, 1)
            

            return product

        for i, (c, d) in enumerate(queries):
            res.append(find_query(c, d))

        return res
            
        
