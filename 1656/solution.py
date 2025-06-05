class OrderedStream:

    def __init__(self, n: int):
        self.values = [None] * n
        self.start = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        index = idKey - 1
        self.values[index] = value

        while self.start < len(self.values) and self.values[self.start]:
            self.start += 1
        return self.values[index: self.start]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
