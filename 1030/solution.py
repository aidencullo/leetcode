class deque:

    class Node:

        def __init__(self, item=None, next=None):
            self.item = item
            self.next = next

    def __init__(self):
        self.head = self.tail = None

    def __bool__(self):
        return bool(self.head)

    def append(self, item):
        new_node = self.Node(item)
        if not self.head:   
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = self.tail.next

    def popleft(self):
        if self.head == self.tail:
            item = self.head.item
            self.head = self.tail = None
            return item
        item = self.head.item
        self.head = self.head.next
        return item
        


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:

        dq = deque()

        r_pair = (rCenter, cCenter)

        dq.append(r_pair)
        

        seen = set()
        seen.add(r_pair)
        cells = []

        while dq:
            pair = dq.popleft()
            r, c = pair
            cells.append(pair)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r = r + dr
                new_c = c + dc
                new_pair = (new_r, new_c)
                if new_r >= 0 and new_r < rows and new_c >= 0 and new_c < cols and new_pair not in seen:
                    seen.add(new_pair)
                    dq.append(new_pair)
                        
        return cells
            
