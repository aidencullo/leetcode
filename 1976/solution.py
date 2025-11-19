class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        def dfs(node, running_time):
            nonlocal shortest_time
            nonlocal ways
            
            if node == n - 1:
                if running_time < shortest_time:
                    shortest_time = running_time
                    ways = 1
                elif running_time == shortest_time:
                    ways += 1
                return
            
            if node in seen:
                return

            seen.add(node)

            for neighbor, time_to in graph[node]:
                dfs(neighbor, running_time + time_to)

            seen.remove(node)

        shortest_time = math.inf
        ways = 0
        seen = set()
        dfs(0, 0)
        return ways
