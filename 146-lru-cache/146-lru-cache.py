class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to nodes
        
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        
        # left: LRU and right: most recently used
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node) -> None:
        # insert at right/end
        prev, next_node = self.right.prev, self.right        
        prev.next = next_node.prev = node
        node.prev = prev
        node.next = next_node
        
        
    def remove(self, node) -> None:
        prev, next_node = node.prev, node.next
        prev.next, next_node.prev = next_node, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            # update most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        # if key exists, remove the value from hashmap and update new value as Node
        # insert the node in DLL
        
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        
        # check the cache capacity
        # if capacity exceeds the defined capacity, evict or remove the least recently used
        # lru will always be at left pointer
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)