from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.diff = SortedDict()
        

    def book(self, start: int, end: int) -> int:
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1
        
        curr = result = 0
        for delta in self.diff.values():
            curr += delta
            result = max(curr, result)
        return result

    
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)