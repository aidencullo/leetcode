from collections import deque

class MyStack:

    def __init__(self):
        self.main = deque()
        self.auxiliary = deque()

    def push(self, x: int) -> None:
        if not self.main:
            self.main.append(x)
            return

        self.auxiliary.append(x)
        while self.main:
            self.auxiliary.append(self.main.popleft())
        self.main, self.auxiliary = self.auxiliary, self.main

    def pop(self) -> int:
        return self.main.popleft()

    def top(self) -> int:
        return self.main[0]

    def empty(self) -> bool:
        return not self.main


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.main()
# param_4 = obj.empty()
