import random

class RandomizedCollection:

    def __init__(self):
        self.data = []
        self.hashmap = defaultdict(set)
        
    def insert(self, val: int) -> bool:
        self.hashmap[val].add(len(self.data))
        self.data.append(val)
        return len(self.hashmap[val]) == 1
    
    def remove(self, val: int) -> bool:
        if not self.hashmap[val]:
            return False
        
        remove, last = self.hashmap[val].pop(), self.data[-1]
        self.data[remove] = last
        self.hashmap[last].add(remove)
        self.hashmap[last].discard(len(self.data) - 1)
        self.data.pop()
        return True
    

    def getRandom(self) -> int:
        return choice(self.data)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()