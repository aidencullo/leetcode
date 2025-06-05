class OrderedStream:

    def __init__(self, n: int):
        self.values = {}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey] = value
        result = []

        while self.ptr in self.values:
            result.append(self.values[self.ptr])
            self.ptr += 1
            
        return result
