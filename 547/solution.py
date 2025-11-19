class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            if node in seen:
                return

            seen.add(node)

            for neighbor, connection in enumerate(isConnected[node]):
                if neighbor != node and connection:
                    dfs(neighbor)

        seen = set()
        nodes = len(isConnected)
        provinces = 0
        for node in range(nodes):
            if node not in seen:
                provinces += 1
                dfs(node)
        return provinces
