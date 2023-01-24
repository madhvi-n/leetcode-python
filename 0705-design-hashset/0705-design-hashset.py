class MyHashSet:

    def __init__(self):
        self.stack = []

    def add(self, key: int) -> None:
        if key not in self.stack:
            self.stack.append(key)

    def remove(self, key: int) -> None:
        if key in self.stack:
            self.stack.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.stack


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)