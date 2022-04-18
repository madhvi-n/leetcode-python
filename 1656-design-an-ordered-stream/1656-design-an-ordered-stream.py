class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * (n + 2)
        self.index = 1

    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id] = value
        if id == self.index:
            while self.stream[self.index]:
                self.index += 1
            return self.stream[id:self.index]
        return []


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)