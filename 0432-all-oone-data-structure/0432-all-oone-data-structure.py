class Block:
    def __init__(self, val=0):
        self.val = val
        self.keys = set()
        self.prev = None
        self.next = None

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev, self.next = None, None

    def insert_next(self, new_block):
        old_next = self.next
        self.next = new_block
        new_block.prev = self
        new_block.next = old_next
        old_next.prev = new_block


class AllOne:
    def __init__(self):
        self.head = Block()  # dummy
        self.tail = Block()  # dummy
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mapping = {}  # key to block

    def inc(self, key):
        if not key in self.mapping:  # find current block and remove key
            current_block = self.head
        else:
            current_block = self.mapping[key]
            current_block.keys.remove(key)

        if current_block.val + 1 != current_block.next.val:  # insert new block
            new_block = Block(current_block.val + 1)
            current_block.insert_next(new_block)
        else:
            new_block = current_block.next

        new_block.keys.add(key)  # update new_block
        self.mapping[key] = new_block  # ... and mapping of key to new_block

        if not current_block.keys and current_block.val != 0:  # delete current block if not seninel
            current_block.remove()

    def dec(self, key):
        if not key in self.mapping:
            return

        current_block = self.mapping[key]
        del self.mapping[key]  # could use self.mapping.pop(key)
        current_block.keys.remove(key)

        if current_block.val != 1:
            if current_block.val - 1 != current_block.prev.val:  # insert new block
                new_block = Block(current_block.val - 1)
                current_block.prev.insert_next(new_block)
            else:
                new_block = current_block.prev
            new_block.keys.add(key)
            self.mapping[key] = new_block

        if not current_block.keys:  # delete current block
            current_block.remove()

    def getMaxKey(self):
        if self.tail.prev.val == 0:
            return ""
        key = self.tail.prev.keys.pop()  # pop and add back to get arbitrary (but not random) element
        self.tail.prev.keys.add(key)
        return key

    def getMinKey(self):
        if self.head.next.val == 0:
            return ""
        key = self.head.next.keys.pop()
        self.head.next.keys.add(key)
        return key

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()