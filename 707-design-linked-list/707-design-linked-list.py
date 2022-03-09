class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.addAtHead(val)
            return
        temp = self.head
        while temp and temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        temp = self.head
        for _ in range(index):
            temp = temp.next

        new_node = Node(val)
        new_node.next = temp
        new_node.prev = temp.prev
        temp.prev.next = new_node
        temp.prev = new_node
        self.size += 1


    def deleteAtHead(self) -> None:
        if self.size is None: return
        if self.size == 1:
            self.head = None
        else :
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.head.prev = None

        self.size -= 1

    def deleteAtTail(self) -> None:
        if self.size is None: return

        temp = self.head
        while temp and temp.next:
            temp = temp.next

        prev_node = temp.prev
        temp.prev = None
        prev_node.next = None
        self.size -= 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0 :
            self.deleteAtHead()
            return

        if index == (self.size - 1):
            self.deleteAtTail()
            return

        temp = self.head
        for _ in range(index):
            temp = temp.next

        prev_node = temp.prev
        after_node = temp.next
        prev_node.next = after_node
        after_node.prev = prev_node
        temp.next = None
        temp.prev = None
        self.size -= 1
