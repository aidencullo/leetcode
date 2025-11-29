class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        from collections import deque

        seen = set()
        q = deque()

        q.append(source)

        while q:
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()

                if node == destination:
                    return True
                
                seen.add(node)
                
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        q.append(neighbor)

        return False

                        

        
