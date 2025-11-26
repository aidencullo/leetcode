class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for start, end, weight in roads:
            graph[start].append((end, weight))
        heap = [(0, 0)]
        visited = set()
        final_distances = {}


        while heap:
            node, current_weight  = heapq.heappop(heap)

            for neighbor, weight in graph[node]:
                if neighbor not in final_distances:
                    final_distances[neighbor] = current_weight + weight
                else:
