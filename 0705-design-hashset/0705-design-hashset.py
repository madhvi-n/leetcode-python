class ListNode:
    def __init__(self, key=-1, next_node=None):
        self.key = key
        self.next = next_node
        
class MyHashSet:

    def __init__(self):
        self.MOD = 1009
        self.map = [ListNode() for _ in range(self.MOD + 1)]
    
    def hashkey(self, key):
        FNV_OFFSET = 10781
        FNV_PRIME = 11261
        
        hash_val = FNV_OFFSET
        key_bytes = str(key).encode('utf-8')
        for byte in key_bytes:
            hash_val = (hash_val ^ byte) * FNV_PRIME
        return hash_val % self.MOD
    
    def add(self, key: int) -> None:
        curr = self.map[self.hashkey(key)]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)
            
    def remove(self, key: int) -> None:
        curr = self.map[self.hashkey(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.map[self.hashkey(key)]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)