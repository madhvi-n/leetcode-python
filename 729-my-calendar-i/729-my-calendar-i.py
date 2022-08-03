import bisect

class MyCalendar:

    def __init__(self):
        self.starts = []
        self.ends = []
        
    def book(self, start: int, end: int) -> bool:
        start_index = bisect.bisect_left(self.starts, end)
        end_index = bisect.bisect_right(self.ends, start)
        
        if start_index == end_index:
            self.starts.insert(start_index, start)
            self.ends.insert(end_index, end)
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)