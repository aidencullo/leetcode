class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for start, end, weight in roads:
            graph[start].append((end, weight))
            graph[end].append((start, weight))
            
        heap = [(0, 0)]
        visited = set()
        distances = {}
        visited = set()
        paths = {}
        paths[0] = 1


        while heap:
            weight, node  = heapq.heappop(heap)

            if node in distances and distances[node] < weight:
                continue

            for neighbor, neighbor_weight in graph[node]:
                if neighbor in visited:
                    continue
                
                other_path_to_neighbor = weight + neighbor_weight
                if neighbor not in distances:
                    distances[neighbor] = other_path_to_neighbor
                    paths[neighbor] = paths[node]
                    heapq.heappush(heap, (other_path_to_neighbor, neighbor))
                elif distances[neighbor] > other_path_to_neighbor:
                    distances[neighbor] = other_path_to_neighbor
                    paths[neighbor] = paths[node]
                    heapq.heappush(heap, (other_path_to_neighbor, neighbor))
                else:
                    paths[neighbor] += paths[node]
                    

            visited.add(node)

        return paths[n - 1]
