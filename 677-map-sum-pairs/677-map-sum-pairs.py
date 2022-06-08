class TrieNode:
    def __init__(self):
        self.children = {}
        self.frequency = 0
        
        
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.dict = {}
        
    def insert(self, key: str, val: int) -> None:
        delta = val - self.dict.get(key, 0)
        self.dict[key] = val
        curr = self.root
        curr.frequency += delta
        
        for char in key:
            curr = curr.children.setdefault(char, TrieNode())
            curr.frequency += delta

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.frequency


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)