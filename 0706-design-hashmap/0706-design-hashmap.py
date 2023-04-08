class ListNode:
    def __init__(self, key=-1, val=-1, next_node=None):
        self.val = val
        self.key = key
        self.next = next_node
        
class MyHashMap:

    def __init__(self):
        self.MOD = 1009
        self.hashmap = [ListNode() for _ in range(self.MOD + 1)]
        
    def hashkey(self, key) -> int:
        return key % self.MOD
    
    def put(self, key: int, value: int) -> None:
        index = self.hashkey(key)
        curr = self.hashmap[index]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)
        
    def get(self, key: int) -> int:
        index = self.hashkey(key)
        curr = self.hashmap[index]   
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1
        
    def remove(self, key: int) -> None:
        index = self.hashkey(key)
        curr = self.hashmap[index]
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)