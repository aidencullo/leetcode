class MyQueue:

    def __init__(self):
        self.main = []
        self.aux = []

    def push(self, x: int) -> None:
        if not self.main:
            self.main.append(x)
            return

        while self.main:
            self.aux.append(self.main.pop())
        self.main.append(x)
        while self.aux:
            self.main.append(self.aux.pop())

    def pop(self) -> int:
        return self.main.pop()
        
    def peek(self) -> int:
        return self.main[-1]

    def empty(self) -> bool:
        return not self.main
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
