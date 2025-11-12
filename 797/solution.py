"""
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.


dq        
[
    (3, [0, 2, 3]),
    (3, [0, 1, 3]),
]

node     path
2        [0, 2]

"""

from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def bfs(root): # root = 0
            dq = deque()
            dq.appendleft((root, [root]))

            while dq:
                node, path = dq.pop() # node = 1, path = [0, 1]

                if node == n - 1: # node = 1, n - 1 = 3 => False
                    paths.append(path)
                    continue

                for neighbor in graph[node]: # graph[1] = [3], path = [0, 1]
                    if neighbor not in path: # neighbor = 3
                        dq.appendleft((neighbor, path + [neighbor]))

        paths = []
        n = len(graph)

        bfs(0)
        return paths
