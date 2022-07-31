class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        
class MyCircularDeque:
    def __init__(self, k: int):
        self.size = k
        self.count = 0
        self.head = Node(-1)
        self.tail = Node(-1, self.head)
        self.head.next = self.tail

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        new = Node(value, self.head, self.head.next)
        new.prev.next = new.next.prev = new
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        new = Node(value, self.tail.prev, self.tail)
        new.prev.next = new.next.prev = new
        self.count += 1
        return True
    
    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.head.next.next.prev, self.head.next = self.head, self.head.next.next
        self.count -= 1
        return True
    
    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.tail.prev.prev.next, self.tail.prev = self.tail, self.tail.prev.prev
        self.count -= 1
        return True
        
    def getFront(self) -> int:
        return self.head.next.value if not self.isEmpty() else -1

    def getRear(self) -> int:
        return self.tail.prev.value if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.count == 0        

    def isFull(self) -> bool:
        return self.count == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()