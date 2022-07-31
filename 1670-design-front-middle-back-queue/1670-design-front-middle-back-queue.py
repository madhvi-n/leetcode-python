class FrontMiddleBackQueue:

    def __init__(self):
        self.front = deque() # for front and middle
        self.back = deque() # for back
        
    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self.balance()
        
    def pushMiddle(self, val: int) -> None:
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        self.front.append(val)
        
    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self.balance()
        
    def popFront(self) -> int:
        val = self.front.popleft() if self.front else -1
        self.balance()
        return val
    
    def popMiddle(self) -> int:
        val = self.front.pop() if self.front else -1
        self.balance()
        return val
    
    def popBack(self) -> int:
        val = (self.back or self.front or [-1]).pop()
        self.balance()
        return val
    
    def balance(self) -> None:
        if len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())
        if len(self.front) < len(self.back):
            self.front.append(self.back.popleft())
            

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()