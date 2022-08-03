class MyCalendarTwo:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        bisect.insort(self.calendar, (start, 1))
        bisect.insort(self.calendar, (end, -1))
        
        bookings = 0
        for time, freq in self.calendar:
            bookings += freq
            if bookings == 3:
                self.calendar.pop(bisect.bisect_left(self.calendar, (start, 1)))
                self.calendar.pop(bisect.bisect_left(self.calendar, (end, -1)))
                return False
        
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)